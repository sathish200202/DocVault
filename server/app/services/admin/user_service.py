from app.models.user_model import User
from app.utils.response import format_response

class AdminUserService:
    @staticmethod
    def get_all_users():
        try:
            users = User.query.all()
            user_list = [
                {
                    "id": user.id,
                    "full_name": user.full_name,
                    "email": user.email,
                    "use_type": user.user_type,
                    "verified": user.verified,
                    "created_at": user.created_at
                } for user in users
            ]
            return format_response(
                data=user_list,
                message="Users retrieved successfully.",
                success=True
            )
        except Exception as e:
            return format_response(
                data=None,
                message="Failed to retrieve users."
            )
        
    @staticmethod
    def get_user_by_id(user_id):
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
        