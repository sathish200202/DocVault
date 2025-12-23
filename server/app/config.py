import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PORT = int(os.getenv("PORT"))
    DEBUG = os.getenv("DEBUG")