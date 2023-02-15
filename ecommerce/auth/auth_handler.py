import time
from typing import Dict

import jwt

from ecommerce.config import JWT_EXPIRES_SECOND, JWT_SECRET, JWT_ALGORITHM


def signJWT(user_id: str) -> Dict[str, str]:
    expires = time.time() + JWT_EXPIRES_SECOND
    payload = {
        "user_id": user_id,
        "expires": expires
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {
        "type": "bearer",
        "access_token": token,
        "expires": expires
    }


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}