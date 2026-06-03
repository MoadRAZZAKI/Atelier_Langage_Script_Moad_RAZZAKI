import logging
import platform
import re
import subprocess

from pydantic import BaseModel, EmailStr, ValidationError

logger = logging.getLogger(__name__)

_IPV4_RE = re.compile(r'\b(\d{1,3}(?:\.\d{1,3}){3})\b')
_EMAIL_RE = re.compile(r'\S+@\S+')


def resoudre_ip(hote: str) -> str | None:

    os_name = platform.system()
    logger.debug("OS: %s — resolving %s via nslookup", os_name, hote)

    try:
        result = subprocess.run(
            ["nslookup", hote],
            capture_output=True,
            text=True,
            timeout=5.0,
        )
    except subprocess.TimeoutExpired:
        logger.warning("nslookup timed out for %s", hote)
        return None
    except FileNotFoundError:
        logger.error("nslookup binary not found on this system")
        return None

    if result.returncode != 0:
        logger.warning(
            "nslookup exited with code %d for %s", result.returncode, hote
        )
        return None

    # Collect every IPv4 found in the output, in order.
    # Strategy: the DNS server address (if IPv4) appears in the first ~3 lines;
    # the resolved address appears later.  On French/localised Windows the
    # section headers are translated ("Adresse :", "Réponse ne faisant pas
    # autorité :"), so we cannot rely on keyword matching.  Instead we harvest
    # all IPv4s and keep track of which belong to the server header block.
    server_ips: set[str] = set()
    answer_ips: list[str] = []

    for i, line in enumerate(result.stdout.splitlines()):
        for m in _IPV4_RE.finditer(line):
            ip = m.group(1)
            if i < 3:           # first 3 lines = server info block
                server_ips.add(ip)
            else:
                answer_ips.append(ip)

    for ip in answer_ips:
        if ip not in server_ips:
            logger.debug("Resolved %s -> %s", hote, ip)
            return ip

    # Last resort: any IPv4 not from the server header
    all_ips = [m.group(1) for m in _IPV4_RE.finditer(result.stdout)]
    for ip in reversed(all_ips):
        if ip not in server_ips:
            logger.debug("Resolved %s -> %s (last-resort)", hote, ip)
            return ip

    logger.warning("Could not extract IPv4 from nslookup output for %s", hote)
    return None


def _whois_cmd(hote: str) -> list[str]:
    """Return the whois command to use, falling back to 'wsl whois' on Windows."""
    if platform.system() == "Windows":
        return ["wsl", "whois", hote]
    return ["whois", hote]


def interroger_whois(hote: str) -> tuple[str | None, str | None]:

    try:
        result = subprocess.run(
            _whois_cmd(hote),
            capture_output=True,
            text=True,
            timeout=10.0,
        )
    except subprocess.TimeoutExpired:
        logger.warning("whois timed out for %s", hote)
        return None, None
    except FileNotFoundError:
        logger.error(
            "whois binary not found — on Linux: apt install whois / on Windows: install WSL or Sysinternals whois"
        )
        return None, None

    if result.returncode != 0:
        logger.warning(
            "whois exited with code %d for %s", result.returncode, hote
        )
        return None, None

    contact: str | None = None
    email: str | None = None

    for line in result.stdout.splitlines():
        if contact is None:
            for pattern in (
                r'Registrant Name:\s*(.+)',
                r'Registrant:\s*(.+)',
            ):
                m = re.match(pattern, line, re.IGNORECASE)
                if m:
                    val = m.group(1).strip()
                    if val and "REDACTED" not in val.upper():
                        contact = val
                        break

        if email is None:
            m = _EMAIL_RE.search(line)
            if m:
                email = m.group(0).rstrip(".,;>)")

    logger.debug("whois for %s -> contact=%r email=%r", hote, contact, email)
    return contact, email


class Domaine(BaseModel):

    hote: str
    ip: str | None
    contact: str | None
    email: EmailStr | None


def collecter(hote: str) -> Domaine:
    logger.info("Collecting data for %s", hote)
    ip = resoudre_ip(hote)
    contact, email_raw = interroger_whois(hote)

    try:
        return Domaine(hote=hote, ip=ip, contact=contact, email=email_raw)
    except ValidationError:
        logger.warning(
            "Extracted email %r for %s failed validation — discarding",
            email_raw,
            hote,
        )
        return Domaine(hote=hote, ip=ip, contact=contact, email=None)
