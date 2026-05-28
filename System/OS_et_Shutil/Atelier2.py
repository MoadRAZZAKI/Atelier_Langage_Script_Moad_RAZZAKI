import argparse, shutil, datetime
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("source", type=Path)
args = parser.parse_args()

horodatage  = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
destination = args.source.parent / f"backup_{horodatage}"

shutil.copytree(args.source, destination)

nb_fichiers = sum(1 for f in destination.rglob("*") if f.is_file())
print(f"Backup créé : {destination}")
print(f"Fichiers copiés : {nb_fichiers}")