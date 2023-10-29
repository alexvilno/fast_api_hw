from pydantic import BaseModel


class Region(BaseModel):
    id: int
    name: str


class Person(BaseModel):
    id: int
    name: str
    sex: str
    reg_id: str
