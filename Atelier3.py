import argparse, socket

parser = argparse.ArgumentParser()
parser.add_argument("--protocole", choices=["tcp", "udp"], required=True)
args = parser.parse_args()

ADDR, TIMEOUT = ("127.0.0.1", 1), 1

if args.protocole == "tcp":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        try:
            s.connect(ADDR)
        except ConnectionRefusedError:
            print("TCP | connexion refusée — le port 1 ne répond pas")
        except TimeoutError:
            print("TCP | connexion refusée — timeout (aucun service sur le port 1)")
else:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(TIMEOUT)
        n = s.sendto(b"ping", ADDR)
        print(f"UDP | datagramme envoyé ({n} octet(s)), aucune confirmation possible")