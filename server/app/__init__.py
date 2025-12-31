from flask import Flask
from app.config import Config
from app.extentions import db, migrate, jwt
from app.utils.jwt_callbacks import is_token_revoked


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    #JWT revocation check
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        return is_token_revoked(jwt_header, jwt_payload)

    from app.routes.auth_route import auth_bp

    app.register_blueprint(auth_bp, url_prefix='/v1/auth')
    
    return app