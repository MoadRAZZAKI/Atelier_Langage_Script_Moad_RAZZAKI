import socket, sys

AF_UNIX = getattr(socket, "AF_UNIX", None)
unix_sock = socket.socket(AF_UNIX, socket.SOCK_STREAM) if AF_UNIX else None

with (
    socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp,
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  as udp,
):
    for name, sock in [("TCP", tcp), ("UDP", udp)]:
        print(f"{name} | fileno={sock.fileno()} | family={sock.family.name} | type={sock.type.name}")

if unix_sock:
    with unix_sock:
        print(f"UNIX | fileno={unix_sock.fileno()} | family={unix_sock.family.name} | type={unix_sock.type.name}")
else:
    print(f"UNIX | fileno=N/A | family=AF_UNIX | type=SOCK_STREAM  (non supporté sur {sys.platform})")


####  Réponse à la question ####
'''
Oui, les trois fileno() sont différents car chaque socket est un fichier au sens Unix socket() est un appel système qui alloue une entrée dans la table des descripteurs de fichiers du processus. Le noyau applique la règle du plus petit entier libre , ainsi chaque nouvel appel socket() reçoit le fd disponible suivant.
'''