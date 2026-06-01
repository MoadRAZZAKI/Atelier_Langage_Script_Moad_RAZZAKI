# Feedback — R00/A6 (Préfixe de longueur 4 octets, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : protocole avec préfixe de longueur `!I` (4 octets big-endian), `sendall`, fonction `recv_exactement` (boucle jusqu'à obtenir n octets), démo sur `socketpair`.

Constat sur ton code :
- ✓ `recv_exactement(sock, n)` : boucle correcte, gestion de l'EOF prématuré avec exception (`EOFError` — le corrigé prend `ConnectionError`, ton choix est tout aussi défendable).
- ✓ `envoyer_message` : `sendall(struct.pack("!I", len(message)) + message)` — parfait, format réseau et atomique.
- ✓ `recevoir_message` : décodage du header puis lecture du payload. Conforme.
- ✓ Démo claire avec affichage `attendu=... reçu=... ok=...`, trois messages de longueurs 1/2/3 octets.
- ✓ La note finale (TCP = flux, `recv(n)` ne garantit pas n octets, d'où la boucle) est juste et au cœur du sujet.

Rien à redire, c'est propre et fidèle au protocole binaire qu'on retrouve dans HTTP/2 ou gRPC.

---
*Évalué sur le commit `b27de7a` (fichier `00_Concepts/Atelier6.py`).*
