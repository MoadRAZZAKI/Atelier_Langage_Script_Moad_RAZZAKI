import socketserver, time

socketserver.TCPServer.allow_reuse_address = True

HOTE = "127.0.0.1"
PORT = 8808

class ServeurMultiClient(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class BonjourHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        ligne = self.rfile.readline().rstrip(b"\n")
        if not ligne:
            return
        print(f"    Reçu de {self.client_address} : {ligne!r}")
        time.sleep(2)  # simule un traitement long — rend le parallélisme visible
        self.wfile.write(b"Bonjour " + ligne + b".\n")

if __name__ == "__main__":
    with ServeurMultiClient((HOTE, PORT), BonjourHandler) as serveur:
        print(f"<<< Serveur multi-client en attente sur {(HOTE, PORT)}")
        print("    (Ctrl-C pour arrêter)")
        serveur.serve_forever()


