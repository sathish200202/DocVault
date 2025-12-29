from app import jwt
import datetime
from flask import current_app
from typing import Optional, Dict
from flask_jwt_extended import create_access_token

def generate_jwt_token(user_id, additional_claims: Optional[Dict] = None):
    try:
        if not user_id:
            raise ValueError("User ID is required to generate JWT token.")
        expires_delta = datetime.timedelta(hours=current_app.config.get("JWT_EXPIRES_IN_HOURS"))
        return create_access_token(
            identity=str(user_id),
            expires_delta=expires_delta,
            additional_claims=additional_claims or {}
        )
    except Exception as e:
        current_app.logger.error(f"Error generating JWT token: {str(e)}")
        return None
    