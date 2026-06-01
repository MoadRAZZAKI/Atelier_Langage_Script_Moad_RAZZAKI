"""Atelier 05 — Mini which (Windows + Unix)"""
 
import subprocess
import sys
import platform
 
if len(sys.argv) < 2:
    print("Usage : python3 atelier_05.py <programme>", file=sys.stderr)
    sys.exit(2)
 
nom = sys.argv[1]
cmd = "where" if platform.system() == "Windows" else "which"
 
try:
    res = subprocess.run([cmd, nom], capture_output=True, text=True)
    if res.returncode == 0:
        # 'where' peut retourner plusieurs lignes, on prend la première
        print(f"{nom} : {res.stdout.splitlines()[0]}")
    else:
        print(f"{nom} : introuvable")
        sys.exit(1)
 
except FileNotFoundError:
    print(f"Erreur : '{cmd}' est introuvable dans le PATH.", file=sys.stderr)
    sys.exit(2)
 