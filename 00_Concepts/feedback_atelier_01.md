# Feedback — Atelier 1 (Moad RAZZAKI)

> **Mise à jour** : le fichier a été déplacé dans `00_Concepts/` ; seule la
> fin de ligne (CRLF→LF) a changé. Contenu identique, évaluation maintenue.

---
*Évalué sur le commit `b27de7a` (fichier `00_Concepts/Atelier1.py`).*

---

## Évaluation précédente (obsolète, commit `22bf8ea`)

# Feedback — Atelier 1 (Moad RAZZAKI)

> **Évaluation à jour** suite à la modification du source. Tu as
> intégré toutes les remarques du feedback précédent — excellent.

## Respect de la consigne

Le script remplit pleinement le contrat :

- validation `len(sys.argv) < 2` avec message d'usage sur stderr
  et `sys.exit(1)` ✓
- `try / except socket.gaierror` autour du `getaddrinfo`,
  message d'erreur sur stderr ✓
- compréhensions sur set (`{r[4][0] for r in enregistrements ...}`)
  pour la déduplication automatique ✓
- `sorted(...)` pour reproductibilité — bonus de robustesse ✓
- total cohérent `len(ipv4) + len(ipv6)` ✓
- format de sortie conforme à l'exemple ✓

C'est un rendu très propre, presque équivalent au corrigé.

## Côté Python (à titre indicatif)

- Style Pythonique avec compréhensions de set + `sorted` —
  pratique idiomatique très lisible.
- L'utilisation de `file=sys.stderr` pour les messages d'erreur
  est la bonne convention (les outils en aval peuvent séparer
  stdout/stderr).
- Pas de fonction `main()` ni de garde — sur 24 lignes, OK.

---
*Évalué sur le commit `22bf8ea` (fichier `Atelier1.py`).*

---

## Évaluation précédente (obsolète, commit `b816d66`)

# Feedback — Atelier 1 (Moad RAZZAKI)

## Respect de la consigne

Le script est très concis (15 lignes) et le format de sortie est
conforme à l'exemple :
- argument CLI lu (sans validation),
- IPv4 et IPv6 séparées via deux compréhensions,
- affichage en deux blocs (`for ip in ipv4`, puis `for ip in
  ipv6`),
- total imprimé avec le format attendu.

Deux écarts :

- **Pas de déduplication** : tes compréhensions prennent toutes
  les entrées, donc si `getaddrinfo` retourne plusieurs tuples pour
  la même adresse (un par socket type), tu auras des doublons à
  l'affichage.
- **Total = `len(enregistrements)`** : nombre brut de tuples
  retournés, pas nombre d'adresses uniques. Une fois la dédup en
  place, il faut basculer sur `len(ipv4) + len(ipv6)`.

## Côté réseau

Le compromis « compréhension + dédup » se fait avec un set :

```python
ipv4 = sorted({r[4][0] for r in enregistrements if r[0] == socket.AF_INET})
ipv6 = sorted({r[4][0] for r in enregistrements if r[0] == socket.AF_INET6})
```

Le `sorted()` est facultatif mais rend la sortie reproductible.

## Côté Python (à titre indicatif)

- Pas de fonction `main()` ni de garde — pas grave sur 15 lignes.
- Pas de gestion de `socket.gaierror` (un domaine inexistant fera
  planter le script) ni de validation `len(sys.argv)` (un appel
  sans argument → `IndexError`).
- Style très Pythonique avec les compréhensions. À garder, juste
  l'enrichir avec le set pour la dédup.

