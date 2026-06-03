# Feedback — R00/A4 (Anatomie d'une paire de sockets, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : `socket.socketpair()` puis afficher pour chaque extrémité `getsockname` / `getpeername` afin de visualiser les 4 endpoints (qui ici se réduisent à des chaînes vides).

Constat sur ton code :
- ✓ Paire créée, boucle sur (A, B), affichage de `fileno`, `getsockname`, `getpeername`. Conforme.
- ✓ `with a, b:` propre.
- ✓ La réponse à la question est très bien : tu expliques que `socketpair()` court-circuite `bind()`, que le canal est un buffer en mémoire dans le noyau, et que l'identité tient au fd. C'est le bon niveau d'explication.
- ⚠ Le corrigé insiste sur la notion de « socket anonyme » et sur le fait qu'aucun tiers ne peut s'y connecter par nom (canal privé). Ta réponse couvre l'essentiel sans nommer le concept — c'est un détail, ton explication reste juste.

---
*Évalué sur le commit `b27de7a` (fichier `00_Concepts/Atelier4.py`).*
