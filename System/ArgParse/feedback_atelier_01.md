# Feedback — S03/A1 (Mini-calculatrice CLI, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : **argparse** avec trois positionnels (float, choices `["+","-","*","/"]`, float), gestion de la division par zéro avec message sur stderr et `sys.exit(1)`.

Constat sur ton code :
- ⚠ **Hors sujet sur le point central** : tu utilises `input()` pour lire `a`, `operateur`, `b` au lieu de `argparse`. Or l'atelier est dans le dossier `ArgParse`, et son objectif est précisément d'apprendre `argparse.ArgumentParser`. Tu n'instancies aucun parser, donc tu ne fais pas l'exercice demandé.
- ✓ Logique métier correcte : conversion en `float`, dispatch sur l'opérateur, calcul juste.
- ✓ Validation de l'opérateur (`if operateur not in (...)`) + `sys.exit(1)` sur stderr — ça fait artisanalement ce que `choices=["+","-","*","/"]` ferait gratuitement avec argparse.
- ✓ Division par zéro : message sur stderr + `sys.exit(1)`. Conforme à ce critère-là.
- ✓ Affichage final propre.

Côté Python : la solution argparse aurait été plus courte (pas besoin de valider à la main les opérateurs) et c'est ce qu'il faut maîtriser pour la suite des ateliers. Reprends l'exercice avec `add_argument("a", type=float)`, `add_argument("operateur", choices=[...])`, etc.

---
*Évalué sur le commit `e2def7f` (fichier `System/ArgParse/Atelier1.py`).*
