ECHELLES = ["celsius", "fahrenheit", "kelvin"]

def vers_celsius(valeur, depuis):
    if depuis == "celsius"   : return valeur
    if depuis == "fahrenheit": return (valeur - 32) * 5/9
    if depuis == "kelvin"    : return valeur - 273.15

def depuis_celsius(valeur, vers):
    if vers == "celsius"     : return valeur
    if vers == "fahrenheit"  : return valeur * 9/5 + 32
    if vers == "kelvin"      : return valeur + 273.15

valeur    = float(input("Valeur : "))
depuis    = input("De (celsius / fahrenheit / kelvin) : ").strip().lower()
vers      = input("Vers (celsius / fahrenheit / kelvin) : ").strip().lower()
precision = input("Précision (décimales, défaut=2) : ").strip()
precision = int(precision) if precision else 2

if depuis not in ECHELLES or vers not in ECHELLES:
    print("Erreur : échelle invalide")
else:
    resultat = depuis_celsius(vers_celsius(valeur, depuis), vers)
    print(f"{valeur:.{precision}f} {depuis} = {resultat:.{precision}f} {vers}")