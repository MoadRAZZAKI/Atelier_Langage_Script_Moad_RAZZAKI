import sys

a        = float(input("Nombre a : "))
operateur = input("Opérateur (+, -, *, /) : ").strip()
b        = float(input("Nombre b : "))

if operateur not in ("+", "-", "*", "/"):
    print("Erreur : opérateur invalide", file=sys.stderr)
    sys.exit(1)

if operateur == "+" : result = a + b
elif operateur == "-": result = a - b
elif operateur == "*": result = a * b
else:
    if b == 0:
        print("Erreur : division par zéro", file=sys.stderr)
        sys.exit(1)
    result = a / b

print(f"{a} {operateur} {b} = {result}")