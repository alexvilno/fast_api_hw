from typing import List, Union, Dict, Any
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from database.db_models import Region
from api.schemas import RegionCreate, RegionUpdate


class CRUDRegion(CRUDBase[Region, RegionCreate, RegionUpdate]):
    def get_all(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100
    ) -> List[Region]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(
        self,
        db: Session,
        *,
        obj_in: RegionCreate,
    ) -> Region:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        db_obj: Region,
        obj_in: Union[RegionUpdate, Dict[str, Any]]
    ) -> Region:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        return super().update(db=db, db_obj=db_obj, obj_in=update_data)


region = CRUDRegion(Region)
