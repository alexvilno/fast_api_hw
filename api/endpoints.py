from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session
from sqlalchemy import select
import api.schemas as schemas
from database.db import get_db
import database.db_models as db_models
from api import filters
from crud import region_crud

points_router = APIRouter()


@points_router.get(
    "/regions_filtered_by_name",
    response_model=list[schemas.RegionBase],
    summary="Информация по всем регионам"
)
def get_regions_filtered_by_name(
        db: Session = Depends(get_db),
        regions_name_filter: filters.RegionFilter = FilterDepends(filters.RegionFilter)
):
    try:
        query = regions_name_filter.filter(select(db_models.Region))
        res = db.execute(query)
        res = res.scalars().all()
        return res
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Error: {err}")


@points_router.get(
    "/regions_all",
    response_model=list[schemas.RegionBase],
    summary="Информация по всем регионам"
)
def get_regions(
        db: Session = Depends(get_db)
):
    try:
        return region_crud.get_regions(db)
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Error: {err}")


@points_router.post(
    "/add_region",
    response_model=schemas.RegionCreate,
    status_code=status.HTTP_201_CREATED,
    summary="Добавить новый регион"
)
def add_region(
        region_in: schemas.RegionCreate,
        db: Session = Depends(get_db)
) -> db_models.Region:
    try:
        return region_crud.create_region(db, region_in)
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=f"Error: {err}")
