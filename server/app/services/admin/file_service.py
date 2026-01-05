from app.models.file_model import File
from app.utils.response import format_response

class AdminFileService:
    @staticmethod
    def get_all_files():
        try:
            files = File.query.all()
            file_list = [
                {
                    "id": file.id,
                    "file_name": file.file_name,
                    "file_size": file.file_size,
                    "mime_type": file.mime_type,
                    "file_owner_name": file.user.full_name,
                    "file_owner_email": file.user.email,
                    "upload_date": file.upload_date.isoformat(),

                } for file in files
            ]
            return format_response(
                data=file_list,
                message="Files retrieved successfully.",
                success=True
            )
        except Exception as e:
            return format_response(
                data=None,
                message="Failed to retrieve files.",
                success=False,
                error=str(e)
            ), 500