from app.extentions import db
from datetime import datetime

class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    s3_key = db.Column(db.String(512), nullable=False, unique=True)
    file_size = db.Column(db.BigInteger, nullable=False)
    mime_type = db.Column(db.String(100), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship("User", backref="files")

    def __repr__(self):
        return f"<File {self.filename}>"