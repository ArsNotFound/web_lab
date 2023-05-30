from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column

from app import db


class News(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    text: Mapped[str]
    img: Mapped[str]


class NewsSchema(BaseModel):
    name: str
    text: str
    img: str

    class Config:
        orm_mode = True
