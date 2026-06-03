# Feedback — R00/A3 (TCP vs UDP face à un port fermé, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : démonstration TCP **ou** UDP au choix sur un port supposé fermé, avec gestion des retours différents des deux protocoles.

Constat sur ton code :
- ✓ Tu vas plus loin que demandé en proposant les deux protocoles via `--protocole {tcp,udp}` — c'est exactement le choix du corrigé.
- ✓ Côté TCP : `settimeout(1)`, `connect`, gestion `ConnectionRefusedError` ET `TimeoutError` séparées. Bien.
- ✓ Côté UDP : `sendto` sans attente de réponse, message clair « aucune confirmation possible ».
- ⚠ Petit décalage de message : ton TimeoutError dit « connexion refusée — timeout » alors que c'est précisément l'absence de réponse SYN-ACK (donc pas un refus). Le corrigé distingue « refus » (RST/ICMP) et « timeout » (rien ne revient).
- ✓ `with socket(...)` partout, settimeout côté UDP aussi (utile si tu voulais lire une éventuelle réponse — ici inutilisé mais sans dommage).

---
*Évalué sur le commit `b27de7a` (fichier `00_Concepts/Atelier3.py`).*
