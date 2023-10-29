from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import cfg

sync_engine = create_engine(
    url=cfg.database_url_psycopg,
    echo=True
)

SessionLocal = sessionmaker(bind=sync_engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
