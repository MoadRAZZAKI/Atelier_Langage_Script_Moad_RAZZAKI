# Feedback — R00/A7 (Boutisme : trois lectures, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : sur `\x00\x00\x00\x2A`, trois lectures (big-endian, little-endian, inversé puis big-endian) et démontrer que les deux dernières donnent la même valeur.

Constat sur ton code :
- ✓ Les trois lectures sont calculées avec `struct.unpack`, équivalent à `int.from_bytes` du corrigé.
- ✓ Tu vérifies explicitement `little == inversé` dans la sortie. Le corrigé utilise `assert` ; ton affichage booléen est tout aussi parlant.
- ✓ L'explication du bonus est juste : par définition, lire en little-endian = lire les octets dans l'ordre inversé d'un big-endian, donc inverser physiquement puis lire en big-endian aboutit nécessairement au même nombre.
- ✓ Bon réflexe pédagogique : « les deux chemins aboutissent au même ordre d'octets avant interprétation ».

Petit détail purement esthétique : le nom de variable `inversé` (avec accent) passe en Python 3 mais beaucoup de styleguides l'évitent. Anecdotique.

---
*Évalué sur le commit `b27de7a` (fichier `00_Concepts/Atelier7.py`).*
