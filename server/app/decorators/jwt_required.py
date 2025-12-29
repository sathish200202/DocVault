from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user_model import User
from app.utils.response import format_response

def jwt_required_user(func):
    """
    Production-level JWT authentication decorator.
    Relies fully on Flask-JWT-Extended.
    """
    @wraps(func)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_id = int(get_jwt_identity())

        user = User.query.get(user_id)
        if not user:
            return format_response(
                data=None,
                message="User not found",
                success=False,
                error="Invalid token"
            ), 404

        return func(*args, user=user, **kwargs)

    return wrapper

