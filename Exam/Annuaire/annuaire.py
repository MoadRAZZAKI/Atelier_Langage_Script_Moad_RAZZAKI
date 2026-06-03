import argparse
import json
import logging
import os
import sys

from dotenv import load_dotenv

load_dotenv()

HOST: str = os.getenv("HOST", "127.0.0.1")
PORT: int = int(os.getenv("PORT", "8888"))

logger = logging.getLogger(__name__)


def _configure_logging(verbosity: int) -> None:
    if verbosity == 0:
        level = logging.WARNING
        fmt = "%(levelname)s: %(message)s"
    elif verbosity == 1:
        level = logging.INFO
        fmt = "%(levelname)s: %(message)s"
    elif verbosity == 2:
        level = logging.DEBUG
        fmt = "%(levelname)s: %(message)s"
    else:
        level = logging.DEBUG
        fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] [%(threadName)s] %(message)s"

    logging.basicConfig(level=level, format=fmt, stream=sys.stderr)



def _serve(args: argparse.Namespace) -> None:
    from serveur import demarrer
    demarrer(HOST, PORT)


def _search(args: argparse.Namespace) -> None:
    from client import cmd_search
    try:
        domaine = cmd_search(args.hote, HOST, PORT)
    except ConnectionRefusedError as exc:
        print(f"Erreur: {exc}", file=sys.stderr)
        sys.exit(1)

    if domaine is None:
        print(f"Domaine '{args.hote}' introuvable.", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(domaine.model_dump(mode="json"), indent=2, ensure_ascii=False))


def _record(args: argparse.Namespace) -> None:
    from client import cmd_record
    try:
        status = cmd_record(args.hote, HOST, PORT)
    except ConnectionRefusedError as exc:
        print(f"Erreur: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Statut: {status}")


def _count(args: argparse.Namespace) -> None:
    from client import cmd_count
    try:
        n = cmd_count(HOST, PORT)
    except ConnectionRefusedError as exc:
        print(f"Erreur: {exc}", file=sys.stderr)
        sys.exit(1)

    print(n)


def _list(args: argparse.Namespace) -> None:
    from client import cmd_list
    try:
        hotes = cmd_list(HOST, PORT)
    except ConnectionRefusedError as exc:
        print(f"Erreur: {exc}", file=sys.stderr)
        sys.exit(1)

    for hote in hotes:
        print(hote)



def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="annuaire",
        description="Annuaire réseau — répertoire de domaines DNS/whois",
    )
    parser.add_argument(
        "-v",
        action="count",
        default=0,
        dest="verbose",
        help="Increase verbosity (-v INFO, -vv DEBUG, -vvv DEBUG+detailed format)",
    )

    sub = parser.add_subparsers(dest="commande", required=True, metavar="commande")

    sub.add_parser("serve", help="Démarrer le serveur TCP")

    p_search = sub.add_parser("search", help="Chercher un domaine")
    p_search.add_argument("hote", help="Nom d'hôte à rechercher")

    p_record = sub.add_parser("record", help="Collecter et enregistrer un domaine")
    p_record.add_argument("hote", help="Nom d'hôte à enregistrer")

    sub.add_parser("count", help="Nombre de domaines enregistrés")
    sub.add_parser("list", help="Lister tous les noms d'hôtes")

    return parser


_HANDLERS = {
    "serve": _serve,
    "search": _search,
    "record": _record,
    "count": _count,
    "list": _list,
}


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    _configure_logging(args.verbose)
    logger.debug("HOST=%s PORT=%d", HOST, PORT)
    _HANDLERS[args.commande](args)


if __name__ == "__main__":
    main()
