import boto3
import uuid
from flask import current_app
from werkzeug.utils import secure_filename

class S3Service:
    @staticmethod
    def get_client():
        return boto3.client(
            's3',
            aws_access_key_id=current_app.config["S3_ACCESS_KEY"],
            aws_secret_access_key=current_app.config["S3_SECRET_KEY"],
            region_name=current_app.config["S3_REGION"]
        )
    

    @staticmethod
    def upload_file(file, user_id):
        s3 = S3Service.get_client()

        filename = secure_filename(file.filename)
        unique_name = f"{uuid.uuid4().hex}_{filename}"
        s3_key = f"users/{user_id}/{unique_name}"

        content_type = file.mimetype if file.mimetype else 'application/octet-stream'

        s3.upload_fileobj(
            file,
            current_app.config["S3_BUCKET_NAME"],
            s3_key,
            ExtraArgs={"ContentType": content_type}

        )

        return {
            "original_filename": filename,
            "stored_filename": unique_name,
            "s3_key": s3_key,
            "file_size": file.content_length,
            "mime_type": file.mimetype
        }
    
    @staticmethod
    def generate_presigned_download_url(s3_key, expires_in):
        s3 = S3Service.get_client()
        url = s3.generate_presigned_url(
            "get_object",
            {
                "Bucket": current_app.config["S3_BUCKET_NAME"],
                "Key": s3_key
            },
            ExpiresIn=expires_in
        )

        return url