from flask import Blueprint

from app.decorators.validate_with_pydantic import validate_with_pydantic
from app.dtos.register_dto import RegisterDTO
from app.dtos.login_dto import LoginDTO
from app.services.auth_service import AuthService
from app.decorators.jwt_required import jwt_required_user

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
@validate_with_pydantic(RegisterDTO)
def register(validated_data):
    return AuthService.user_register(validated_data)

@auth_bp.route("/login", methods=["POST"])
@validate_with_pydantic(LoginDTO)
def login(validated_data):
    return AuthService.user_login(validated_data)

@auth_bp.route("/profile", methods=["GET"])
@jwt_required_user
def profile(user):
    return AuthService.get_profile(user.id)