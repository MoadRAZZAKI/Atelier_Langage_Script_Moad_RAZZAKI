# Feedback — S06/A2 (Backup horodaté, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : `shutil.copytree` vers `backup_<strftime YYYYMMDD_HHMMSS>/` à côté de la source, compter les fichiers copiés.

Constat sur ton code :
- ✓ argparse pour le chemin source (`type=Path`) — propre.
- ✓ `datetime.datetime.now().strftime("%Y%m%d_%H%M%S")` — format conforme.
- ✓ `args.source.parent / f"backup_{horodatage}"` — backup à côté de la source comme demandé.
- ✓ `shutil.copytree(args.source, destination)` — appel direct, sans options exotiques, parfait.
- ✓ Comptage des fichiers avec `rglob("*")` filtré par `is_file()` — correct.
- ⚠ Aucune vérification que `args.source` est bien un dossier (`is_dir()`). Si on passe un fichier ou un chemin inexistant, `copytree` plante avec une trace Python — pas catastrophique mais le corrigé lève proprement `NotADirectoryError`.
- ⚠ Pas de mode démo (le corrigé fournit une arborescence factice si aucun argument n'est passé, pour ne pas toucher au FS utilisateur). C'est un bonus, pas un critère obligatoire.

---
*Évalué sur le commit `5158883` (fichier `System/OS_et_Shutil/Atelier2.py`).*
