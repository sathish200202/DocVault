from app.models.user_model import User
from app.models.file_model import File
from app.utils.response import format_response

class AdminDashboardService:
    @staticmethod
    def get_dashboard_stats():
        try:
            
            total_users = User.query.filter_by(user_type='user').count()
            total_admins = User.query.filter_by(user_type='admin').count()
            total_super_admins = User.query.filter_by(user_type='super_admin').count()
            total_files = File.query.count()

            stats = {
                "total_super_admins": total_super_admins,
                "total_users": total_users,
                "total_admins": total_admins,
                "total_files": total_files
            }
            return format_response(
                data=stats,
                message="Admin dashboard statistics retrieved successfully.",
                success=True
            ), 200
        except Exception as e:
            return format_response(
                data=None,
                message="Failed to retrieve admin dashboard statistics.",
                success=False,
                error=str(e)
            ), 500