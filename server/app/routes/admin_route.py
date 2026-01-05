from flask import Blueprint
from app.decorators.admin_required import admin_required
from app.services.admin.admin_dashboard import AdminDashboardService
from app.services.admin.user_service import AdminUserService
from app.services.admin.file_service import AdminFileService
from app.utils.response import format_response

admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/dashboard", methods=["GET"])
@admin_required
def admin_dashboard(user):
    if user.user_type != "admin" and user.user_type != "super_admin":
        return format_response(
            success=False,
            message="Admin privileges required."
        ), 403
    return AdminDashboardService.get_dashboard_stats()

@admin_bp.route("/users", methods=["GET"])
@admin_required
def get_all_users(user):
    return AdminUserService.get_all_users()

@admin_bp.route("/users/<int:user_id>", methods=["GET"])
@admin_required
def get_user_by_id(user, user_id):
    return AdminUserService.get_user_by_id(user_id)

@admin_bp.route("/files", methods=["GET"])
@admin_required
def get_all_files(user):
    return AdminFileService.get_all_files()