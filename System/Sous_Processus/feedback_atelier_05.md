# Feedback — S08/A5 (Mini `which`, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : `subprocess.run(["which", nom])`, gérer code 0 (afficher chemin) vs code != 0 (introuvable + `exit(1)`), `FileNotFoundError` si `which` lui-même manque, `exit(1)` sur erreur.

Constat sur ton code :
- ✓ Vérif `len(sys.argv) < 2` → `exit(2)` (le corrigé fait pareil pour les erreurs d'usage).
- ✓ `subprocess.run([cmd, nom], capture_output=True, text=True)` — exactement la bonne signature.
- ✓ Distinction `returncode == 0` (affichage du chemin) vs `!= 0` (« introuvable » + `sys.exit(1)`). Conforme.
- ✓ Capture `FileNotFoundError` séparée → message dédié + `sys.exit(2)`.
- ✓ Bonus inattendu et bienvenu : tu détectes Windows avec `platform.system()` et utilises `where` au lieu de `which`. Tu prends même la peine de `splitlines()[0]` parce que `where` peut renvoyer plusieurs lignes. Excellent réflexe.
- ⚠ Pas de `timeout=` sur `subprocess.run` (le corrigé met `timeout=2.0` et capture `TimeoutExpired`). Pour `which`/`where` ça ne risque rien, mais c'est une bonne habitude générale.
- ⚠ Petit écart de codes retour : le corrigé renvoie `sys.exit(1)` à la fois pour « introuvable » et pour « which manquant » ; tu mets `1` pour introuvable et `2` pour which manquant. Plus précis chez toi, mais s'écarte du critère qui demande `exit(1)`. Anecdotique.

---
*Évalué sur le commit `eef02f2` (fichier `System/Sous_Processus/Atelier5.py`).*
