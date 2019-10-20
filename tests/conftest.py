import logging

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import Session, sessionmaker

from mypkg.database.model import Base
from mypkg.util.config import Config


@pytest.fixture(scope='session')
def config() -> Config:
    return Config('example.toml')


@pytest.fixture(scope='session')
def engine(config: Config) -> Engine:
    return create_engine(config.db.uri_test)


@pytest.fixture(scope='session')
def SessionMaker(engine: Engine) -> Config:
    return sessionmaker(bind=engine)


@pytest.fixture(scope='function')
def db_session(engine: Engine, SessionMaker: sessionmaker) -> Session:
    Base.metadata.create_all(engine)
    session = SessionMaker()
    yield session
    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture(scope='function')
def logger() -> logging.Logger:
    return logging.getLogger()
