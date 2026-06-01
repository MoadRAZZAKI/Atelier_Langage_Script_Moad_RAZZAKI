# Feedback — R03/A5 (ThreadingMixIn + TCPServer, RAZZAKI Moad)

## Respect de la consigne

Critères attendus : créer une sous-classe de `TCPServer` qui hérite aussi de `ThreadingMixIn` (mixin **en premier** dans la MRO), handler avec `time.sleep` pour rendre le parallélisme observable.

Constat sur ton code :
- ✓ `class ServeurMultiClient(socketserver.ThreadingMixIn, socketserver.TCPServer)` — mixin en premier, ordre correct. C'est exactement ce qu'il faut.
- ✓ `time.sleep(2)` dans `handle()` pour simuler un traitement long.
- ✓ `StreamRequestHandler` avec `self.rfile.readline()` / `self.wfile.write(...)` — bonne utilisation du framing ligne.
- ✓ `allow_reuse_address = True` activé (au niveau classe `TCPServer` au lieu d'attribut de ta sous-classe — les deux marchent, le corrigé préfère le mettre dans la sous-classe pour ne pas polluer globalement).
- ✓ `serve_forever()` dans un `with`, messages de démarrage clairs.
- ⚠ Le corrigé affiche `threading.current_thread().name` pour rendre le parallélisme **visible** dans les logs. Tu te contentes d'afficher `client_address` — ça marche, mais on ne voit pas explicitement que deux clients sont traités en parallèle. Petit plus pédagogique manqué.

---
*Évalué sur le commit `e2def7f` (fichier `03_SocketServer/Atelier5.py`).*
