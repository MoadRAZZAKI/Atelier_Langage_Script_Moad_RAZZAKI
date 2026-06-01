"""Atelier 03 — Extraire un .tar.gz en sécurité"""
 
import tarfile
import tempfile
from pathlib import Path
 
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
 
    # 1. Créer l'archive
    fichiers = {"notes.txt": "notes\n", "config.ini": "[x]\n", "data.csv": "a,b\n1,2\n"}
    for nom, contenu in fichiers.items():
        (tmp / nom).write_text(contenu)
 
    archive = tmp / "archive.tar.gz"
    with tarfile.open(archive, "w:gz") as tar:
        for f in fichiers:
            tar.add(tmp / f, arcname=f)
    print(f"Archive créée : {[m.name for m in tarfile.open(archive).getmembers()]}")
 
    # 2. Extraire en sécurité
    cible = tmp / "cible"
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall(cible, filter="data")
    print(f"Extrait dans : {cible}")
 
    # 3. Lister les fichiers extraits
    for f in sorted(cible.rglob("*")):
        if f.is_file():
            print(f"  {f.name}  ({f.stat().st_size} octets)")