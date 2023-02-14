from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name : str = Field(...)
    email : EmailStr = Field(...)
    password : str = Field(...)

    # def __init__(self, name, email, password):
    #     self.name = name
    #     self.email= email
    #     self.password= password
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
