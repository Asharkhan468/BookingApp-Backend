from jose import jwt
from datetime import datetime, timedelta
from app.config.settings import settings

ALGORITHM = "HS256"

def create_access_token(data: dict):
    payload = data.copy()

    payload["exp"] = datetime.utcnow() + timedelta(days=7)

    token = jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=ALGORITHM
    )

    return token