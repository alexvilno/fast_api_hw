from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()
metadata = Base.metadata


class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    sex = Column(String, nullable=True)
    reg_id = Column(Integer, ForeignKey("regions.id"))
