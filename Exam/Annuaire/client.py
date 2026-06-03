import json
import logging
import socket

from collecte import Domaine

logger = logging.getLogger(__name__)

_TIMEOUT = 15
_BUFSIZE = 4096


def _envoyer(host: str, port: int, msg: dict) -> dict:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(_TIMEOUT)
        try:
            s.connect((host, port))
        except ConnectionRefusedError:
            raise ConnectionRefusedError(
                f"Cannot connect to {host}:{port} — is the server running?"
            )

        payload = json.dumps(msg) + "\n"
        s.sendall(payload.encode())

        buf = b""
        while b"\n" not in buf:
            chunk = s.recv(_BUFSIZE)
            if not chunk:
                break
            buf += chunk

    first_line = buf.split(b"\n")[0]
    return json.loads(first_line)


def cmd_search(hote: str, host: str = "127.0.0.1", port: int = 8888) -> Domaine | None:
    """Send SEARCH and return a Domaine, or None if not found."""
    response = _envoyer(host, port, {"cmd": "SEARCH", "arg": hote})
    if "error" in response:
        logger.debug("SEARCH %s -> %s", hote, response["error"])
        return None
    return Domaine(**response)


def cmd_record(hote: str, host: str = "127.0.0.1", port: int = 8888) -> str:
    response = _envoyer(host, port, {"cmd": "RECORD", "arg": hote})
    status = response.get("status", "UNKNOWN")
    logger.debug("RECORD %s -> %s", hote, status)
    return status


def cmd_count(host: str = "127.0.0.1", port: int = 8888) -> int:
    response = _envoyer(host, port, {"cmd": "COUNT"})
    return int(response.get("count", 0))


def cmd_list(host: str = "127.0.0.1", port: int = 8888) -> list[str]:
    response = _envoyer(host, port, {"cmd": "LIST"})
    return list(response.get("hotes", []))
