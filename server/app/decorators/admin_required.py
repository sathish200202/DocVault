from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user_model import User
from app.utils.response import format_response

def admin_required(func):
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
        if user.user_type != "admin" and user.user_type != "super_admin":
            return format_response(
                success=False,
                message="Admin privileges required."
            ), 403
        return func(user, *args, **kwargs)
    return wrapper