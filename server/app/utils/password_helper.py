from passlib.context import CryptContext

_pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    if not password:
        raise ValueError("Password cannot be empty")
    return _pwd_context.hash(password)
    

def validate_password(password: str, hashed_password: str):
    if not password or not hashed_password:
        return False
    return _pwd_context.verify(password, hashed_password)