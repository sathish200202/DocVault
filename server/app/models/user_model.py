from app.extentions import db
from datetime import datetime
from app.utils.password_helper import hash_password, validate_password


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    user_type = db.Column(db.String(50), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password: str):
        self.hashed_password = hash_password(password)
    
    def check_password(self, password: str) -> bool:
        return validate_password(password, self.hashed_password)