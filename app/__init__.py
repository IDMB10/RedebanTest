import os
from flask import Flask
from .config import get_config
from .db import init_engine, remove_session, get_session
from .models import Base
from .routes import bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())


    # DB
    engine = init_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    Base.metadata.create_all(bind=engine)
    app.teardown_appcontext(remove_session)


    # Routes
    app.register_blueprint(bp)


    @app.get("/health")
    def health_root():
        return {"status": "ok"}, 200

    return app