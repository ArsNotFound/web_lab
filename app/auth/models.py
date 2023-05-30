from sqlalchemy.orm import Mapped, mapped_column

from app import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[bytes]
    email: Mapped[str] = mapped_column(unique=True)
