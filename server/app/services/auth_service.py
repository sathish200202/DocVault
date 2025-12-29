from app.models.user_model import User
from app.utils.response import format_response
from app.extentions import db
from app.utils.jwt_utils import generate_jwt_token

class AuthService:
    @staticmethod
    def user_register(validated_data):
        try:
            existing_user = User.query.filter_by(email=validated_data.email).first()
            if existing_user:
                return format_response(
                    message="User with this email already exists",
                    success=False,
                    error="User already exists"
                ), 409
            
            user_type = validated_data.user_type or "user"
            new_user = User(
                full_name=validated_data.full_name,
                email=validated_data.email,
                user_type=user_type
            )
            new_user.set_password(validated_data.password)
            db.session.add(new_user)
            db.session.commit()
            return format_response(
                data={
                    "id": new_user.id,
                    "full_name": new_user.full_name,
                    "email": new_user.email,
                    "user_type": new_user.user_type
                },
                message="User registered successfully"
            ), 201
        except Exception as e:
            db.session.rollback()
            return format_response(data=None, message="User registration failed", success=False, error=str(e)), 500
    
    @staticmethod
    def user_login(validated_data):
        try:
            user = User.query.filter_by(email=validated_data.email).first()
            if not user:
                return format_response(
                    None,
                    "No account found with this email. Please register.",
                    False,
                    "User not found"
                ), 404
            if not user.check_password(validated_data.password):
                return format_response(
                    None,
                    "Incorrect password. Please try again.",
                    False,
                    "Authentication failed"
                ), 401
            
            token = generate_jwt_token(user.id, additional_claims={"user_type": user.user_type})
            return format_response({
                "token": token,
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "full_name": user.full_name,
                    "user_type": user.user_type
                }
            }, "Login successful"), 200

        except Exception as e:
            return format_response(None, "Login failed due to server error", False, str(e)), 500
        
    @staticmethod
    def get_profile(user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                return format_response(None, "User not found", False), 404
            
            profile = {
                "user": {
                "id": user.id,
                "email": user.email,
                "full_name": user.full_name,
                "user_type": user.user_type,
                "createdAt": user.created_at.isoformat(),
                }
            }
           
            return format_response(profile, "Profile retrieved successfully")
        
        except Exception as e:
            return format_response(None, "Failed to retrieve profile", False, str(e)), 500