from pydantic import BaseModel


class News(BaseModel):
    name: str
    text: str
    img: str
