from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
import api.schemas as schemas
from database.db import get_db
import database.db_models as db_models

points_router = APIRouter()


@points_router.get(
    "/regions",
    response_model=list[schemas.Region],
    summary="Информация по всем регионам"
)
def get_regions_all(
        db: Session = Depends(get_db)
):
    try:
        query = select(db_models.Region)
        res = db.execute(query)
        res = res.scalars().all()
        return res
    except Exception as err:
        raise HTTPException(status_code=503, detail=f"Ошибка: {err}")
