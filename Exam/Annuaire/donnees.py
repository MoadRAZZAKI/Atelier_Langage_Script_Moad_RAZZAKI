import logging
from pathlib import Path

from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

from collecte import Domaine

logger = logging.getLogger(__name__)

BDD_PATH = Path(__file__).parent / "domaines.db"


class Base(DeclarativeBase):
    pass


class DomaineORM(Base):

    __tablename__ = "domaines"

    hote: Mapped[str] = mapped_column(String, primary_key=True)
    ip: Mapped[str | None] = mapped_column(String, nullable=True)
    contact: Mapped[str | None] = mapped_column(String, nullable=True)
    email: Mapped[str | None] = mapped_column(String, nullable=True)


engine = create_engine(f"sqlite:///{BDD_PATH}")
Base.metadata.create_all(engine)


def _orm_to_pydantic(row: DomaineORM) -> Domaine:
    return Domaine(
        hote=row.hote,
        ip=row.ip,
        contact=row.contact,
        email=row.email,
    )


def enregistrer(domaine: Domaine) -> None:
    with Session(engine) as session:
        if session.get(DomaineORM, domaine.hote) is not None:
            raise ValueError(f"Domain {domaine.hote!r} already exists in the database")
        row = DomaineORM(
            hote=domaine.hote,
            ip=domaine.ip,
            contact=domaine.contact,
            email=str(domaine.email) if domaine.email else None,
        )
        session.add(row)
        session.commit()
        logger.info("Registered: %s", domaine.hote)


def lister() -> list[Domaine]:
    with Session(engine) as session:
        rows = session.query(DomaineORM).all()
        return [_orm_to_pydantic(r) for r in rows]


def chercher(hote: str) -> Domaine | None:
    with Session(engine) as session:
        row = session.get(DomaineORM, hote)
        return _orm_to_pydantic(row) if row is not None else None
