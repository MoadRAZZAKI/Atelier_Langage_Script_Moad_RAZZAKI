import socket

a, b = socket.socketpair()
with a, b:
    for name, sock in [("A", a), ("B", b)]:
        print(f"Socket {name} | fileno={sock.fileno()} "
              f"| local='{sock.getsockname()}' "
              f"| peer='{sock.getpeername()}'")


#### Réponse à la question ####


'''
socketpair() crée deux sockets AF_UNIX connectés directement dans le noyau, sans aucun appel à bind(). Sans bind(), aucune adresse n'est attribuée, les sockets sont anonymes : getsockname() et getpeername() retournent '' car il n'y a littéralement rien à retourner.

Sur TCP/IPv4, le tuple (IP, port) sert à router les paquets sur le réseau, il est indispensable. Ici, les deux sockets vivent dans le même noyau : le canal est un simple buffer en mémoire, le noyau sait déjà où envoyer les données sans adresse. L'identité de chaque extrémité, c'est son fd, rien d'autre.

'''