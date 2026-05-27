import sys, datetime

message     = input("Message : ").strip()
horodatage  = datetime.datetime.now().isoformat(timespec="seconds")

with open("app.log", "a", encoding="utf-8") as f:
    f.write(f"{horodatage} {message}\n")

print(f"Ajouté : {horodatage} {message}")