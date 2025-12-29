from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager



db = SQLAlchemy()

migrate = Migrate()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

jwt = JWTManager()