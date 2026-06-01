# Feedback — R00/A8 (Modes d'attente, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : comparer deux modes d'attente sur un socket vide — `socket.timeout` (via `settimeout`) et l'usage de `select.select()` pour attendre sans bloquer. Bonus : expliquer pourquoi on ne peut pas mesurer simplement le mode bloquant.

Constat sur ton code :
- ✓ Cas `settimeout(0.2)` parfaitement mesuré, sortie en ms claire.
- ⚠ Tu compares à `setblocking(False)` (= `settimeout(0)`) au lieu d'utiliser `select.select()` comme le suggérait le critère. Le résultat numérique est cohérent (≈ 0 ms), mais on perd la démonstration pédagogique de `select` comme primitive d'attente multiplexée. Le corrigé fait aussi le choix de `setblocking(False)` plutôt que `select`, donc ton choix est en fait celui du corrigé — note quand même que `select.select([b], [], [], 0.2)` aurait été une 3ᵉ variante intéressante.
- ✓ La capture `(TimeoutError, BlockingIOError)` est élégante : tu n'écris la mesure qu'une fois pour les deux cas.
- ✓ Le bonus est bien répondu : sans timeout, `recv()` bloque indéfiniment, il faudrait un 2ᵉ thread pour envoyer ou fermer afin de débloquer la mesure.

---
*Évalué sur le commit `b27de7a` (fichier `00_Concepts/Atelier8.py`).*
