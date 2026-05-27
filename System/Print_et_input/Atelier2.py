from datetime import date

prenom = input("Ton prénom : ")
age    = int(input("Ton âge : "))
annee  = date.today().year - age

print(f"Bonjour, {prenom}, tu as {age} ans, donc tu es né(e) vers {annee}.")