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

---
*Évalué sur le commit `b816d66` (fichier `Atelier1.py`).*
