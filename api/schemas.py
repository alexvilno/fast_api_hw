from pydantic import BaseModel


class RegionBase(BaseModel):
    id: int
    name: str


class RegionCreate(RegionBase):
    pass


class Person(BaseModel):
    id: int
    name: str
    sex: str
    reg_id: int | None


class PersonCreate(Person):
    pass
