import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PORT = int(os.getenv("PORT"))
    DEBUG = os.getenv("DEBUG")

    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True'

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT"))

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = (f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    JWT_EXPIRES_IN_HOURS = int(os.getenv("JWT_EXPIRES_IN_HOURS"))
    SECRET_KEY = os.getenv("SECRET_KEY")

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

    #AWS S3 Configuration
    S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")
    S3_ACCESS_KEY = os.getenv("AWS_S3_ACCESS_KEY_ID")
    S3_SECRET_KEY = os.getenv("AWS_S3_SECRET_ACCESS_KEY")
    S3_REGION = os.getenv("AWS_REGION_NAME")
    SIGN_URL_EXPIRATION = int(os.getenv("SIGN_URL_EXPIRATION"))