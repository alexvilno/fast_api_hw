from pydantic import BaseModel


class RegionBase(BaseModel):
    name: str


class RegionCreate(RegionBase):
    pass


class Person(BaseModel):
    id: int
    name: str
    sex: str
    reg_id: str
