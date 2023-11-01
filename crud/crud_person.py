from typing import List

from sqlalchemy.orm import Session

from api.schemas import PersonCreate, PersonUpdate
from crud.base import CRUDBase
from database.db_models import Person


class CRUDPerson(CRUDBase[Person, PersonCreate, PersonUpdate]):
    def get_all_by_reg_id(
            self,
            db: Session,
            reg_id: int,
            skip: int = 0,
            limit: int = 100
    ) -> List[Person]:
        return (
            db.query(Person)
            .filter(Person.reg_id == reg_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


person = CRUDPerson(Person)
