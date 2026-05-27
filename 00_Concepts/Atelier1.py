import sys
import socket

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <nom_de_domaine>", file=sys.stderr)
    sys.exit(1)

nom = sys.argv[1]

try:
    enregistrements = socket.getaddrinfo(nom, None)
except socket.gaierror as e:
    print(f"Erreur : Impossible de résoudre le nom '{nom}' ({e})", file=sys.stderr)
    sys.exit(1)

ipv4 = sorted({r[4][0] for r in enregistrements if r[0] == socket.AF_INET})
ipv6 = sorted({r[4][0] for r in enregistrements if r[0] == socket.AF_INET6})

for ip in ipv4:
    print(f"IPv4 : {ip}")
for ip in ipv6:
    print(f"IPv6 : {ip}")

print(f"Total : {len(ipv4) + len(ipv6)} enregistrement(s)")
