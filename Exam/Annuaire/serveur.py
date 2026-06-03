import json
import logging
import socketserver

from collecte import collecter
from donnees import chercher, enregistrer, lister

logger = logging.getLogger(__name__)


class AnnuaireHandler(socketserver.StreamRequestHandler):

    def handle(self) -> None:
        logger.debug("New connection from %s", self.client_address)
        try:
            for raw in self.rfile:
                line = raw.strip()
                if not line:
                    continue
                try:
                    msg = json.loads(line)
                except json.JSONDecodeError as exc:
                    self._send({"error": f"INVALID_JSON: {exc}"})
                    continue
                response = self._dispatch(msg)
                self._send(response)
        except ConnectionResetError:
            logger.debug("Client %s disconnected", self.client_address)

    def _send(self, obj: dict) -> None:
        payload = json.dumps(obj) + "\n"
        self.wfile.write(payload.encode())
        self.wfile.flush()

    def _dispatch(self, msg: dict) -> dict:
        cmd = str(msg.get("cmd", "")).upper()
        arg = str(msg.get("arg", ""))

        if cmd == "SEARCH":
            domaine = chercher(arg)
            if domaine is None:
                return {"error": "NOT_FOUND"}
            return domaine.model_dump(mode="json")

        if cmd == "RECORD":
            try:
                domaine = collecter(arg)
                enregistrer(domaine)
                return {"status": "OK"}
            except ValueError:
                return {"status": "ALREADY_EXISTS"}
            except Exception as exc:
                logger.exception("Unexpected error while recording %s", arg)
                return {"status": "ERROR", "msg": str(exc)}

        if cmd == "COUNT":
            return {"count": len(lister())}

        if cmd == "LIST":
            return {"hotes": [d.hote for d in lister()]}

        return {"error": f"UNKNOWN_CMD: {cmd!r}"}


class AnnuaireServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    allow_reuse_address = True


def demarrer(host: str, port: int) -> None:
    with AnnuaireServer((host, port), AnnuaireHandler) as server:
        logger.info("Annuaire server listening on %s:%d", host, port)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            logger.info("Shutting down server")
