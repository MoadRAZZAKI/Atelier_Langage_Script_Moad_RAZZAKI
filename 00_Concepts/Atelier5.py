import socket

def recv_ligne(sock: socket.socket) -> bytes:
    chunks = []
    while (octet := sock.recv(1)) and octet != b"\n":
        chunks.append(octet)
    return b"".join(chunks)

a, b = socket.socketpair()
with a, b:
    a.sendall(b"bonjour\nle monde\n")
    print(recv_ligne(b))
    print(recv_ligne(b))


#### réponse au bonus ####

'''
recv(1) fonctionne correctement mais est lent car chaque octet lu déclenche un appel système — un aller-retour coûteux entre ton programme et le noyau.
La solution est de lire par gros blocs (recv(4096)) et de stocker le surplus dans un buffer en mémoire. On cherche ensuite le \n dans ce buffer sans aucun appel système supplémentaire — et si la ligne suivante est déjà dans le buffer, on ne rappelle même pas recv.'''