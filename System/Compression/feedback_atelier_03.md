# Feedback — S07/A3 (Extraire un .tar.gz en sécurité, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : créer une archive factice dans un `tempfile`, l'extraire avec `tar.extractall(cible, filter="data")`, puis lister les fichiers extraits.

Constat sur ton code :
- ✓ `tempfile.TemporaryDirectory()` pour tout isoler. Bien.
- ✓ Création de trois fichiers (notes.txt, config.ini, data.csv) puis ajout dans une archive `w:gz`. Conforme.
- ✓ `tar.extractall(cible, filter="data")` — le **filter="data"** est exactement le point critique de l'atelier (sécurité contre les chemins hors-cible, depuis Python 3.12). Parfait.
- ✓ Listage final avec `rglob("*")` + `is_file()` + taille, exactement ce qui était demandé.
- ⚠ Ligne 19 : tu rouvres l'archive avec `tarfile.open(archive)` sans la fermer dans un `with`. Petite fuite de ressource (pas grave dans un script court).
- ⚠ Le corrigé crée une arborescence avec un sous-dossier (`src/a.py`, etc.) pour mieux illustrer le `arcname` et le rglob ; tes fichiers sont tous à la racine. Détail.

Bon réflexe sécurité globalement : le `filter="data"` n'est pas anodin, c'est précisément ce qui distingue cet atelier d'un simple `extractall`.

---
*Évalué sur le commit `eef02f2` (fichier `System/Compression/Atelier3.py`).*
