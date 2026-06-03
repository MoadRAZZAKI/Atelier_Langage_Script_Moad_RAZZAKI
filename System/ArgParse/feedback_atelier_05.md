# Feedback — S03/A5 (Convertisseur de température, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : argparse avec `--from`/`--to` (mots-clés Python → `dest="depuis"`/`dest="vers"`), `choices=["celsius","fahrenheit","kelvin"]`, conversion via le **pivot Celsius**, précision optionnelle.

Constat sur ton code :
- ⚠ **Pas d'argparse** : tu lis `valeur`, `depuis`, `vers`, `precision` au clavier avec `input()`. Le titre du dossier est `ArgParse` — l'enjeu de l'atelier est exactement d'utiliser `add_argument("--from", dest="depuis", choices=...)` etc. Tu refais la validation à la main alors qu'argparse fait tout ça gratuitement (et c'est le point pédagogique).
- ✓ Le **pivot Celsius** est bien là : `vers_celsius` puis `depuis_celsius`. Formules justes (32, ×5/9, +273.15).
- ✓ Précision avec valeur par défaut 2, gérée correctement.
- ✓ Validation des échelles présente (à la main).
- ✓ Format de sortie aligné avec ce qu'attend le corrigé : `f"{valeur:.{precision}f} {depuis} = {resultat:.{precision}f} {vers}"`.

Côté Python : reprends en exposant les options `--from`/`--to` via argparse, c'est l'occasion d'apprendre `dest=` (incontournable car `from` est mot-clé). Le squelette métier est déjà bon, il ne reste qu'à brancher le parser dessus.

---
*Évalué sur le commit `e2def7f` (fichier `System/ArgParse/Atelier5.py`).*
