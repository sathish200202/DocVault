from flask import Flask
from app.config import Config
from app.extentions import db, migrate, jwt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.models.user_model import User

    from app.routes.auth_route import auth_bp

    app.register_blueprint(auth_bp, url_prefix='/v1/auth')
    
    return app