import socket, struct

def recv_exactement(sock: socket.socket, n: int) -> bytes:
    chunks = []
    restant = n
    while restant > 0:
        chunk = sock.recv(restant)
        if not chunk:
            raise EOFError("connexion fermée prématurément")
        chunks.append(chunk)
        restant -= len(chunk)
    return b"".join(chunks)

def envoyer_message(sock: socket.socket, message: bytes) -> None:
    sock.sendall(struct.pack("!I", len(message)) + message)

def recevoir_message(sock: socket.socket) -> bytes:
    longueur = struct.unpack("!I", recv_exactement(sock, 4))[0]
    return recv_exactement(sock, longueur)

# Test
messages = [b"a", b"bb", b"ccc"]

a, b = socket.socketpair()
with a, b:
    for msg in messages:
        envoyer_message(a, msg)
    for msg in messages:
        recu = recevoir_message(b)
        print(f"attendu={msg!r:8} reçu={recu!r:8} ok={recu == msg}")


'''
recv_exactement est indispensable car TCP est un flux, un seul recv(n) ne garantit pas de recevoir exactement n octets d'un coup. La boucle accumule jusqu'à avoir le compte exact.

'''

