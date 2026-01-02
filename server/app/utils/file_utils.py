# import os
# from wekzeug.utils import secure_filename
# import uuid
# from datetime import datetime
# from flask import current_app
# from app.config import Config

# def save_uploaded_file(file):
#     if not file or file.filename == "":
#             raise ValueError("No file provided")
    
#     original_filename = secure_filename(file.filename)
#     # Strong unique filename
#     unique_filename = f"{uuid.uuid4().hex}_{original_filename}"
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     saved_filename = f"{timestamp}_{unique_filename}"

#     upload_root = current_app.config["UPLOAD_FOLDER"]

#     upload_folder = os.path.join(current_app.root_path, upload_root)
#     os.makedirs(upload_folder, exist_ok=True)

#     file_path = os.path.join(upload_folder, saved_filename)
#     file.save(file_path)

#     return f"/{upload_root}/{saved_filename}"


import os
import uuid
from flask import current_app
from werkzeug.utils import secure_filename



def save_uploaded_file(file, user_id: int) -> dict:
        if not file or file.filename == "":
            raise ValueError("No file provided")

        # Sanitize filename
        original_filename = secure_filename(file.filename)

        # Strong unique filename
        unique_filename = f"{uuid.uuid4().hex}_{original_filename}"

        # User-isolated folder
        upload_root = current_app.config["UPLOAD_FOLDER"]
        user_folder = os.path.join(upload_root, "users", str(user_id))
        os.makedirs(user_folder, exist_ok=True)

        file_path = os.path.join(user_folder, unique_filename)
        file.save(file_path)

        return {
            "stored_filename": unique_filename,
            "original_filename": original_filename,
            "file_path": file_path,
            "file_size": os.path.getsize(file_path),
            "mime_type": file.mimetype
        }
