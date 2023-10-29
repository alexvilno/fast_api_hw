from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from database.db_models import Person
from api.schemas import PersonCreate


def get_persons(session: Session) -> list[Person]:
    stmt = select(Person).order_by(Person.name)
    res: Result = session.execute(stmt)
    persons = res.scalars().all()
    return list(persons)
