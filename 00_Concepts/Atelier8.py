import socket, time

def mesurer(mode: str, sock: socket.socket) -> None:
    t0 = time.perf_counter()
    try:
        sock.recv(1)
    except (TimeoutError, BlockingIOError):
        pass
    durée = time.perf_counter() - t0
    print(f"{mode:<25} : {durée*1000:.1f} ms")

a, b = socket.socketpair()
with a, b:
    b.settimeout(0.2)
    mesurer("settimeout(0.2)", b)

a, b = socket.socketpair()
with a, b:
    b.setblocking(False)
    mesurer("setblocking(False)", b)



#### Pourquoi on ne peut pas tester le mode bloquant simplement ? ####

'''
En mode bloquant, recv() attend des données et ne rend jamais la main si personne n'envoie rien, ainsi le script se met en pause pour toujours.
Pour le tester, il faudrait quelqu'un qui envoie une donnée pendant que tu mesures, c'est-à-dire un deuxième thread qui joue le rôle de l'émetteur pendant que le premier mesure le temps d'attente.

'''