import datetime

def journaliser(chemin: str, message: str) -> None:
    horodatage = datetime.datetime.now().isoformat(timespec="seconds")
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(f"{horodatage} {message}\n")

message = input("Message : ").strip()
journaliser("app.log", message)
print(f"Ajouté dans app.log : {message}")