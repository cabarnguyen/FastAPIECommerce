from fastapi import APIRouter, Depends, status, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from . import models
from . import services
from . import validator

router = APIRouter(tags=['Users'], prefix='/user')

@router.post('/', status_code= status.HTTP_201_CREATED)
async def create_user_registration(user: models.User = Body(...)):
    valid_user = await validator.verify_email_exist(user.email)
    print(valid_user)
    if valid_user:
        raise HTTPException(
            status_code= 400,
            detail= "the user with this email exits in the system"
        )

    user = jsonable_encoder(user)
    new_student = await services.new_user_register(user)
    return models.ResponseModel(new_student, "that ok")