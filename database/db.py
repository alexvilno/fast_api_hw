from sqlalchemy import create_engine

from config import cfg

engine = create_engine(
    url=cfg.database_url_psycopg,
    echo=True
)
