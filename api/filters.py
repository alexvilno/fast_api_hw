from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional
from database import db_models


class RegionFilter(Filter):
    name__ilike: Optional[str] = None

    class Constants(Filter.Constants):
        model = db_models.Region
