import sys
import socket

nom = sys.argv[1]
enregistrements = socket.getaddrinfo(nom, None)

ipv4 = [r[4][0] for r in enregistrements if r[0] == socket.AF_INET]
ipv6 = [r[4][0] for r in enregistrements if r[0] == socket.AF_INET6]

for ip in ipv4:
    print(f"IPv4 : {ip}")
for ip in ipv6:
    print(f"IPv6 : {ip}")

print(f"Total : {len(enregistrements)} enregistrement(s)")