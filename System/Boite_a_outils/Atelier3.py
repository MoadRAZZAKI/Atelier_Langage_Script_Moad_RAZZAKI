"""Atelier 03 — Token URL-safe dans un .env temporaire"""
 
import secrets
import tempfile
from pathlib import Path
 
token = secrets.token_urlsafe(32)
 
with tempfile.TemporaryDirectory() as tmp:
    env_file = Path(tmp) / ".env"
    env_file.write_text(f"TOKEN={token}\n")
 
    ligne = env_file.read_text().strip()
    _, _, valeur = ligne.partition("=")
 
    print(f"fichier .env : {env_file}")
    print(f"contenu     : {ligne}")
    print(f"lu          : {valeur}")
    print(f"identique   : {secrets.compare_digest(token, valeur)}")