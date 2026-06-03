import pytest
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

import donnees
from collecte import Domaine


@pytest.fixture(autouse=True)
def temp_db(monkeypatch):
    test_engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    donnees.Base.metadata.create_all(test_engine)
    monkeypatch.setattr(donnees, "engine", test_engine)
    yield
    test_engine.dispose()



def _dom(
    hote: str = "example.com",
    ip: str | None = "1.2.3.4",
    contact: str | None = "Alice",
    email: str | None = "alice@example.com",
) -> Domaine:
    return Domaine(hote=hote, ip=ip, contact=contact, email=email)


def test_enregistrer_et_chercher():
    donnees.enregistrer(_dom())
    found = donnees.chercher("example.com")
    assert found is not None
    assert found.hote == "example.com"
    assert found.ip == "1.2.3.4"
    assert found.contact == "Alice"


def test_chercher_absent_retourne_none():
    result = donnees.chercher("inexistant.com")
    assert result is None


def test_enregistrer_doublon_leve_valueerror():
    donnees.enregistrer(_dom())
    with pytest.raises(ValueError, match="already exists"):
        donnees.enregistrer(_dom())


def test_enregistrer_hotes_differents():
    donnees.enregistrer(_dom("a.com"))
    donnees.enregistrer(_dom("b.com"))
    assert donnees.chercher("a.com") is not None
    assert donnees.chercher("b.com") is not None


def test_lister_vide():
    assert donnees.lister() == []


def test_lister_retourne_tous():
    donnees.enregistrer(_dom("a.com"))
    donnees.enregistrer(_dom("b.com"))
    donnees.enregistrer(_dom("c.com"))
    liste = donnees.lister()
    assert len(liste) == 3
    hotes = {d.hote for d in liste}
    assert hotes == {"a.com", "b.com", "c.com"}


def test_lister_retourne_des_domaines():
    donnees.enregistrer(_dom())
    liste = donnees.lister()
    assert all(isinstance(d, Domaine) for d in liste)


def test_champs_nuls_preserves():
    d = Domaine(hote="null.com", ip=None, contact=None, email=None)
    donnees.enregistrer(d)
    found = donnees.chercher("null.com")
    assert found is not None
    assert found.ip is None
    assert found.contact is None
    assert found.email is None


def test_ip_nulle_contact_present():
    d = _dom("partial.com", ip=None, contact="Bob", email=None)
    donnees.enregistrer(d)
    found = donnees.chercher("partial.com")
    assert found is not None
    assert found.ip is None
    assert found.contact == "Bob"



def test_email_round_trip():
    donnees.enregistrer(_dom(email="user@domain.org"))
    found = donnees.chercher("example.com")
    assert found is not None
    assert str(found.email) == "user@domain.org"
