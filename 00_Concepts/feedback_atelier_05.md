# Feedback — R00/A5 (recv_ligne maison, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : implémenter `recv_ligne(sock) -> bytes` à la main par boucle `recv(1)` jusqu'au `\n` exclu, puis démonstration sur une paire et bonus sur l'inefficacité.

Constat sur ton code :
- ✓ La fonction est correcte et concise : `while (octet := sock.recv(1)) and octet != b"\n":` couvre à la fois l'EOF (recv renvoie `b""`, falsy) et le délimiteur. Élégant.
- ⚠ Subtilité : quand `recv(1)` rend `b""` (EOF), la boucle s'arrête et tu renvoies les chunks accumulés — c'est correct. Mais si jamais tu appelais `recv_ligne` une 3e fois sans données disponibles, tu bloquerais (le sender n'a pas été fermé). Le corrigé ferme `a` immédiatement après `send`, ce qui rend l'EOF visible et permet une 3e lecture qui retourne `b""`. Pédagogiquement, fermer côté émetteur est plus parlant.
- ✓ La démonstration affiche bien les deux lignes attendues.
- ✓ La réponse au bonus (un appel système par octet, buffer interne + recv par blocs comme `makefile()`) est juste et bien expliquée.

---
*Évalué sur le commit `b27de7a` (fichier `00_Concepts/Atelier5.py`).*
