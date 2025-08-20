from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


_engine = None
_Session = None


def init_engine(db_url: str):
    global _engine, _Session
    _engine = create_engine(db_url, future=True)
    _Session = scoped_session(sessionmaker(bind=_engine, autoflush=False, autocommit=False))
    return _engine


def get_session():
    return _Session


def remove_session(_=None):
    if _Session:
        _Session.remove()