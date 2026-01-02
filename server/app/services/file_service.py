from app.extentions import db
from app.models.file_model import File
from app.utils.response import format_response
from app.services.s3_service import S3Service
from flask import current_app


class FileService:
    @staticmethod
    def upload_file(file, user_id):
        try:
            file_info = S3Service.upload_file(file, user_id)
            new_file = File(
                user_id=user_id,
                file_name=file_info["original_filename"],
                file_size=file_info["file_size"],
                mime_type=file_info["mime_type"],
                s3_key=file_info["s3_key"]  # reused field for local storage
            )

            db.session.add(new_file)
            db.session.commit()

            return format_response(
                success=True,
                message="File uploaded successfully",
                data={
                    "file_id": new_file.id,
                    "file_name": new_file.file_name,
                    "file_size": new_file.file_size,
                    "mime_type": new_file.mime_type,
                    "upload_date": new_file.upload_date
                }

            )
        except Exception as e:
            db.session.rollback()
            return format_response(success=False, message=str(e))
        

    @staticmethod
    def get_user_files(user_id):
        try:
            files = File.query.filter_by(user_id=user_id).all()
            file_list = [
                {
                    "file_id": f.id,
                    "file_name": f.file_name,
                    "file_size": f.file_size,
                    "mime_type": f.mime_type,
                    "upload_date": f.upload_date
                }
                for f in files
            ]
            return format_response(
                success=True,
                message="Files retrieved successfully",
                data=file_list
            )
        except Exception as e:
            return format_response(success=False, message=str(e))


    @staticmethod
    def delete_selected_files(file_ids, user_id):
        return
    
    @staticmethod
    def get_file_by_id(file_id, user_id):
        try:
            file = File.query.filter_by(id=file_id, user_id=user_id).first()
            if not file:
                return format_response(
                    success=False,
                    message="File not found"
                )
            return format_response(
                success=True,
                message="File retrieved successfully",
                data={
                    "file_id": file.id,
                    "file_name": file.file_name,
                    "file_size": file.file_size,
                    "mime_type": file.mime_type,
                    "upload_date": file.upload_date
                }
            )
        except Exception as e:
            return format_response(success=False, message=str(e))
        

    @staticmethod
    def delete_file_by_id(file_id, user_id):
        try:
            file = File.query.filter_by(id=file_id, user_id=user_id).first()
            if not file:
                return format_response(
                    success=False,
                    message="File not found"
                )
            print(file.s3_key)
            s3 = S3Service.get_client()
            s3.delete_object(
                Bucket=current_app.config["S3_BUCKET_NAME"],
                Key=file.s3_key
            )
            db.session.delete(file)
            db.session.commit()
            return format_response(
                success=True,
                message="File deleted successfully"
            )
        except Exception as e:
            db.session.rollback()
            return format_response(success=False, message=str(e))
        

    @staticmethod
    def generate_download_link(file_id, user_id):
        try:
            file = File.query.filter_by(id=file_id, user_id=user_id).first()
            if not file:
                return format_response(
                    success=False,
                    message="File not found"
                )
            expires_in = current_app.config["SIGN_URL_EXPIRATION"]
            url = S3Service.generate_presigned_download_url(
                s3_key=file.s3_key,
                expires_in=expires_in
            )
            return format_response(
            success=True,
            message="Download URL generated",
            data={"download_url": url}
        )
        except Exception as e:
             return format_response(success=False, message=str(e))
