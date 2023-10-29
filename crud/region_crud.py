from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from database.db_models import Region
from api.schemas import RegionCreate


def get_regions(session: Session) -> list[Region]:
    stmt = select(Region).order_by(Region.name)
    res: Result = session.execute(stmt)
    regions = res.scalars().all()
    return list(regions)


def create_region(session: Session, region_in: RegionCreate) -> Region:
    region = Region(**region_in.model_dump())
    session.add(region)
    session.commit()
    return region
