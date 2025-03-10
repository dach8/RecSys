from sqlmodel import SQLModel, Session, create_engine
from contextlib import contextmanager
from .config import get_settings

engine = create_engine(
    url=get_settings().DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10
)

@contextmanager
def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    # import app.models.account
    # import app.models.user
    # import app.models.item
    # import app.models.prediction
    # import app.models.ml
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
