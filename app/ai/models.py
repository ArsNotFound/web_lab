from pydantic import BaseModel, validator
from pydantic.networks import HttpUrl
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db


class NeuralNetworkCategory(db.Model):
    __tablename__ = "neural_category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    networks: Mapped[list["NeuralNetwork"]] = relationship(back_populates="category")


class NeuralNetworkCategorySchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class NeuralNetwork(db.Model):
    __tablename__ = "neural"

    slug: Mapped[str] = mapped_column(String(128), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("neural_category.id"))
    category: Mapped["NeuralNetworkCategory"] = relationship(back_populates="networks")
    img: Mapped[str]
    tasks: Mapped[str]
    field: Mapped[str]
    short_desc: Mapped[str]
    desc: Mapped[str]
    url: Mapped[str]


class NeuralNetworkSchema(BaseModel):
    name: str
    slug: str | None = None
    category: NeuralNetworkCategorySchema
    img: str
    tasks: str
    field: str
    short_desc: str
    desc: str
    url: HttpUrl

    @validator('slug', always=True)
    def slug_validator(cls, v, values) -> str:
        if not values.get('slug'):
            return str(values['name']).lower().replace(' ', '_')
        else:
            return str(values['slug']).lower().replace(' ', '_')

    class Config:
        orm_mode = True


class NeuralNetworkSchemaIn(BaseModel):
    name: str
    url: HttpUrl
    tasks: str
    field: str
    desc: str
