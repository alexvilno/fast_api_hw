from pydantic import BaseModel


class Base(BaseModel):

    class Config:
        from_attributes = True


class RegionBase(BaseModel):
    name: str


class Region(RegionBase):
    id: int


class RegionCreate(RegionBase):
    pass


class RegionUpdate(RegionBase):
    pass


class Person(BaseModel):
    id: int
    name: str
    sex: str
    reg_id: int | None


class PersonCreate(Person):
    pass


class PersonUpdate(Person):
    pass


class PersonsInRegionResponse(Base):
    id: int
    name: str
    people: list[Person] | None
