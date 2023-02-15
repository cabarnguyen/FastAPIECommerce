from typing import Optional
from .models import User
from ecommerce.db import users

async def verify_email_exist(email: str) -> Optional[User]:
    return users.find_one({"email": email})


