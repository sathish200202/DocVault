from app.models.token_blacklist import TokenBlacklist
from app.extentions import db


def is_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return db.session.query(
        TokenBlacklist.id
    ).filter_by(jti=jti).scalar() is not None