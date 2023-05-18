from pydantic import BaseModel, validator
from pydantic.networks import HttpUrl


class NeuralNetworkCategory(BaseModel):
    name: str


class NeuralNetwork(BaseModel):
    name: str
    slug: str | None = None
    category: NeuralNetworkCategory
    img: str
    tasks: str
    field: str
    short_desc: str
    desc: str
    url: HttpUrl

    @validator('slug', always=True)
    def slug_validator(cls, v, values) -> str:
        return str(values['name']).lower().replace(' ', '_')


class NeuralNetworkIn(BaseModel):
    name: str
    url: HttpUrl
    tasks: str
    field: str
    desc: str


class News(BaseModel):
    name: str
    text: str
    img: str
