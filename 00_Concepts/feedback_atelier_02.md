# Feedback — R00/A2 (Trois familles de sockets, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : instancier trois sockets (AF_INET STREAM, AF_INET DGRAM, AF_UNIX STREAM) et afficher pour chacun `fileno`, `family.name`, `type.name`. AF_UNIX peut être absent sous Windows, donc une garde est tolérée.

Constat sur ton code :
- ✓ Les deux sockets AF_INET (TCP et UDP) sont créés dans un `with` imbriqué, fileno + family.name + type.name sont bien imprimés.
- ✓ Tu gères proprement le cas Windows avec `getattr(socket, "AF_UNIX", None)` puis un `with unix_sock:` séparé — c'est plus défensif que le corrigé qui suppose AF_UNIX disponible.
- ⚠ Le socket UNIX est créé hors du `with` principal, donc les trois ne coexistent pas simultanément quand tu lis leurs fileno. Le corrigé voulait illustrer la règle « plus petit entier libre » sur trois fd ouverts en même temps ; ici tu vois la valeur reprise après libération. Pas une faute, mais l'observation pédagogique est légèrement décalée.
- ✓ La réponse à la question (fd uniques, règle du plus petit entier libre, allocation par le noyau) est juste et bien formulée.

---
*Évalué sur le commit `b27de7a` (fichier `00_Concepts/Atelier2.py`).*
