# Feedback — S13/A3 (Token URL-safe dans un .env temporaire, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : `secrets.token_urlsafe(32)`, écriture dans un `.env` placé dans un `tempfile.TemporaryDirectory()`, relecture, vérification d'égalité avec `secrets.compare_digest`.

Constat sur ton code :
- ✓ `secrets.token_urlsafe(32)` — bonne primitive.
- ✓ `TemporaryDirectory()` puis `Path(tmp) / ".env"` — propre, le fichier disparaît automatiquement.
- ✓ Écriture avec `write_text(f"TOKEN={token}\n")`.
- ✓ Relecture + `partition("=")` pour extraire la valeur. Concis et correct pour une seule clé.
- ✓ `secrets.compare_digest(token, valeur)` — exactement le point pédagogique de l'atelier (comparaison à temps constant, on traite le token comme un secret).
- ⚠ Le corrigé pousse un cran plus loin avec un mini-parseur `.env` (saut des lignes vides et commentaires `#`, retour d'un dict). Ta version monoligne marche mais ne survit pas à un `.env` plus réaliste. Pour ce niveau d'exercice c'est suffisant.

Bon réflexe : tu n'as pas écrit le token en clair dans une variable globale exportée, tout reste dans le scope local.

---
*Évalué sur le commit `eef02f2` (fichier `System/Boite_a_outils/Atelier3.py`).*
