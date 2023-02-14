from ecommerce.db import users

async def new_user_register(user_data: dict) -> dict:
    user =  users.insert_one(user_data)
    new_user = users.find_one({"_id": user.inserted_id})
    return {
        "id": str(new_user["_id"]),
        "name": new_user["name"],
        "email": new_user["email"]
    }