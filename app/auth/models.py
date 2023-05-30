from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[bytes]
    email: Mapped[str] = mapped_column(unique=True)

    added_networks: Mapped[list["NeuralNetwork"]] = relationship(back_populates="added_by")


class UserSchema(BaseModel):
    id: int
    login: str
    email: str

    class Config:
        orm_mode = True


from app.ai.models import NeuralNetwork
