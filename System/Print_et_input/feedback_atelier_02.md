# Feedback — S01/A2 (Prénom + âge → année de naissance, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : `input` du prénom et de l'âge, calcul de l'année de naissance via `date.today().year`, gestion de `ValueError` si l'âge n'est pas un entier.

Constat sur ton code :
- ✓ `from datetime import date` + `date.today().year - age` : conforme.
- ✓ Message de sortie propre, `f-string` bien formatée avec accord né(e).
- ⚠ Pas de gestion de `ValueError` : `int(input("Ton âge : "))` plante en stack-trace brut si l'utilisateur tape « vingt ». Le corrigé encapsule dans une boucle `while True` avec un message « ce n'est pas un entier, réessaye ». C'est le point clé du critère « gestion ValueError ».
- ⚠ Pas non plus de `.strip()` sur le prénom (le corrigé le fait, utile si on tape un espace par mégarde).
- ⚠ Pas de bloc `if __name__ == "__main__":` ni de fonction `main()` — pas faux, mais le corrigé structure ainsi pour rendre réutilisable.

---
*Évalué sur le commit `1db90e1` (fichier `System/Print_et_input/Atelier2.py`).*
