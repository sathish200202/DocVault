from flask import Blueprint, request
from app.decorators.jwt_required import jwt_required_user
from app.services.file_service import FileService
from app.utils.response import format_response


file_bp = Blueprint("file", __name__)

@file_bp.route("/upload", methods=["POST"])
@jwt_required_user
def upload_file(user):
    file = request.files["file"]
    if not file:
        return format_response(
            None,
            "File is required",
            False,
            "Missing file"
        ), 400
    return FileService.upload_file(file, user.id)

@file_bp.route("/my-files", methods=["GET"])
@jwt_required_user
def get_user_files(user):
    page = request.args.get("page", 1)
    limit = request.args.get("limit", 10)
    sort = request.args.get("sort", "desc")

    return FileService.get_user_files(
        user_id=user.id,
        page=page,
        limit=limit,
        sort=sort
    )

@file_bp.route("/my-files/<int:file_id>", methods=["GET"])
@jwt_required_user
def get_user_file_by_id(file_id, user):
    return FileService.get_file_by_id(file_id, user.id)

@file_bp.route("/my-files/<int:file_id>", methods=["DELETE"])
@jwt_required_user
def delete_user_file_by_id(file_id, user):
    return FileService.delete_file_by_id(file_id, user.id)

@file_bp.route("/my-files/<int:file_id>/download", methods=["GET"])
@jwt_required_user
def generate_user_file_url(file_id, user):
    return FileService.generate_download_link(file_id, user.id)