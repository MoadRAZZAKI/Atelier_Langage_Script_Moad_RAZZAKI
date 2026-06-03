# Annuaire réseau

Un annuaire de domaines en réseau développé avec Python 3.12+. Pour chaque nom d'hôte,
l'application collecte l'adresse IP, le contact whois et l'e-mail whois, les persiste
dans une base SQLite locale et les expose via un serveur TCP.

---

## Prérequis

### Outils système

```bash
# Debian/Ubuntu
sudo apt install whois dnsutils   # whois + nslookup

# macOS
brew install whois                # nslookup est intégré

# Windows
# nslookup est intégré ; installer whois depuis https://docs.microsoft.com/sysinternals
```

### Paquets Python

```bash
cd Exam/Annuaire
python -m venv .venv
source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

### Environnement

Copier `.env.example` vers `.env` et ajuster si besoin :

```bash
cp .env.example .env
```

Valeurs par défaut : `HOST=127.0.0.1`, `PORT=8888`.

---

## Structure du projet

```
Annuaire/
├── collecte.py          # Résolution IP (nslookup) + whois + modèle Pydantic
├── donnees.py           # ORM SQLAlchemy (domaines.db)
├── serveur.py           # Serveur TCP (protocole JSON-lines)
├── client.py            # Fonctions client TCP
├── annuaire.py          # Point d'entrée CLI (argparse)
├── tests/
│   └── test_donnees.py  # Tests pytest de la couche données
├── conftest.py          # Configuration pytest (sys.path)
├── requirements.txt
├── .env.example
└── README.md
```

---

## Utilisation

### 1 — Démarrer le serveur

```bash
python annuaire.py serve
# ou avec les logs détaillés :
python annuaire.py -vv serve
```

Le serveur écoute sur `HOST:PORT` (par défaut `127.0.0.1:8888`).  
Arrêter avec **Ctrl+C**.

### 2 — Enregistrer un domaine

Résout l'IP et interroge whois, puis stocke le résultat :

```bash
python annuaire.py record mines-ales.fr
# Statut: OK

python annuaire.py record mines-ales.fr
# Statut: ALREADY_EXISTS
```

### 3 — Rechercher un domaine

```bash
python annuaire.py search mines-ales.fr
```

```json
{
  "hote": "mines-ales.fr",
  "ip": "91.121.67.85",
  "contact": "Association des anciens élèves",
  "email": "contact@mines-ales.fr"
}
```

### 4 — Compter les domaines enregistrés

```bash
python annuaire.py count
# 3
```

### 5 — Lister tous les noms d'hôtes

```bash
python annuaire.py list
# mines-ales.fr
# google.com
# github.com
```

### Niveaux de verbosité

| Option | Niveau  | Format du log                                      |
|--------|---------|----------------------------------------------------|
| (rien) | WARNING | `NIVEAU: message`                                  |
| `-v`   | INFO    | `NIVEAU: message`                                  |
| `-vv`  | DEBUG   | `NIVEAU: message`                                  |
| `-vvv` | DEBUG   | `horodatage NIVEAU [fichier:ligne] [thread] msg`   |

---

## Lancer les tests

```bash
pytest -v
```

Les tests utilisent une base SQLite en mémoire et ne touchent pas `domaines.db`.

---

## Justification du protocole (Protocole C — JSON lines)

Le serveur utilise du **JSON délimité par des sauts de ligne** (un objet JSON par ligne) :

```
{"cmd": "SEARCH", "arg": "mines-ales.fr"}\n
{"hote": "mines-ales.fr", "ip": "91.121.67.85", ...}\n
```

**Pourquoi le Protocole C plutôt que les alternatives ?**

| Critère | JSON lines | texte brut | HTTP/REST |
|---------|--------------------------|--------------------------|-------------------------|
| Données structurées | Oui — types JSON natifs | Non — parsing manuel | Oui |
| Délimitation | Saut de ligne (trivial) | Personnalisée | En-têtes HTTP |
| Dépendances | stdlib uniquement (`json`) | Aucune | `flask`/`fastapi` |
| Débogage avec netcat | Oui | Oui | Difficile |
| Extensible | Oui | Difficile | Oui |
| Surcoût | Minimal | Minimal | Élevé |

Le Protocole C apporte la structure de HTTP sans la lourdeur d'une pile HTTP,
et la lisibilité du texte brut sans le parsing fragile. Chaque commande est un
objet JSON autonome, ce qui rend le protocole sans état, facile à tester et
simple à étendre.
