from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.db import get_db
import database.db_models as db_models
from api import filters
from crud.crud_region import region
from crud.crud_person import person
from typing import Any
from api import schemas

points_router = APIRouter()


@points_router.get(
    "/regions_filtered_by_name",
    response_model=list[schemas.Region],
    summary="Информация по всем регионам"
)
def get_regions_filtered_by_name(
        db: Session = Depends(get_db),
        regions_name_filter: filters.RegionFilter = FilterDepends(filters.RegionFilter)
) -> Any:
    try:
        query = regions_name_filter.filter(select(db_models.Region))
        res = db.execute(query)
        res = res.scalars().all()
        return res
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Error: {err}")


@points_router.get(
    "/regions_all",
    response_model=list[schemas.Region],
    summary="Информация по всем регионам"
)
def get_regions(
        db: Session = Depends(get_db)
):
    try:
        regions = region.get_all(db=db)
        return regions
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Error: {err}")


@points_router.post(
    "/region_create",
    response_model=schemas.RegionBase,
    summary="Создать новый регион"
)
def create_region(
        region_in: schemas.RegionCreate,
        db: Session = Depends(get_db)
):
    try:
        reg = region.create(db=db, obj_in=region_in)
        return reg
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Error: {err}")


@points_router.post(
    "/region_update/{reg_id}",
    response_model=schemas.RegionBase,
    summary="Обновить инфо о регионе"
)
def update_region(
        reg_id: int,
        region_upd: schemas.RegionCreate,
        db: Session = Depends(get_db)
):
    try:
        reg = region.get(db, req_id=reg_id)
        if not reg:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Error: does not exists")
        reg = region.update(db=db, db_obj=reg, obj_in=region_upd)
        return reg
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Error: {err}")


@points_router.post(
    "/region_delete/{reg_id}",
    response_model=schemas.Region,
    summary="Удалить регион по id"
)
def delete_region(
        reg_id: int,
        db: Session = Depends(get_db)
):
    reg = region.get(db, req_id=reg_id)
    if not reg:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error: does not exists")
    reg = region.remove(db=db, id=reg_id)
    return reg


@points_router.get(
    "/persons_by_reg_id/{reg_id}",
    response_model=list[schemas.Person],
    summary="Все люди по ID региона"
)
def get_persons_by_reg_id(
        reg_id: int,
        db: Session = Depends(get_db)
):
    persons = person.get_all_by_reg_id(db=db, reg_id=reg_id)
    return persons


@points_router.get(
    "/regions_with_people",
    response_model=schemas.PersonsInRegionResponse,
    summary="Регион и его население"
)
def get_population(
        reg_id: int,
        db: Session = Depends(get_db)
):
    reg = region.get(db, req_id=reg_id)
    persons: list[schemas.Person] = []
    for p in person.get_all_by_reg_id(db, reg_id=reg_id):
        persons.append(
            schemas.Person(
                id=p.id,
                name=p.name,
                sex=p.sex,
                reg_id=p.reg_id
            )
        )
    response = schemas.PersonsInRegionResponse(
        id=reg.id,
        name=reg.name,
        people=persons
    )
    return response
