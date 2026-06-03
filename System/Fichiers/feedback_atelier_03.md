# Feedback — S05/A3 (Journal horodaté, RAZZAKI Moad)

> **Ré-évaluation à jour** : code inchangé sur le fond — fonction conforme, lecture du message via `input()` (au lieu de `argparse`/CLI), pas d'évolution notable.

## Respect de la consigne

Critères attendus : fonction `journaliser(chemin, message)` qui ouvre le fichier en mode `"a"` et écrit `<horodatage ISO> <message>` (`datetime.now().isoformat()`).

Constat sur ton code :
- ✓ Ouverture en mode append (`'a'`).
- ✓ Horodatage `datetime.datetime.now().isoformat(timespec="seconds")` — ISO, à la seconde.
- ✓ Encodage explicite `utf-8`.
- ✓ Signature et type hints conformes : `journaliser(chemin: str, message: str) -> None`.
- ⚠ Pas de garde `if __name__ == "__main__":` : l'appel `input(...)` et l'écriture s'exécutent dès l'import du module. Sans impact pour un script exécuté directement, mais c'est un anti-pattern pour la réutilisation.
- ⚠ Pas de docstring sur `journaliser`.

---
*Évalué sur le commit `5158883` (fichier `System/Fichiers/Atelier3.py`).*

---

## Évaluation précédente (obsolète, commit `48a7fa7`)

# Feedback — S05 Atelier 3 (Journal horodaté, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : fonction `journaliser(chemin, message)` qui ouvre le fichier en mode `"a"`
et écrit `<horodatage ISO> <message>` (datetime.now().isoformat())

Constat sur ton code :

- ✓ ouverture en mode append (`'a'`)
- ✓ utilisation de `datetime`
- ✓ encoding explicite
