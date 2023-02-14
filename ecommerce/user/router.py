from fastapi import APIRouter, Depends, status, Body
from fastapi.encoders import jsonable_encoder
from . import models
from . import services

router = APIRouter(tags=['Users'], prefix='/user')

@router.post('/', status_code= status.HTTP_201_CREATED)
async def create_user_registration(user: models.User = Body(...)):
    user = jsonable_encoder(user)
    new_student = await services.new_user_register(user)
    return models.ResponseModel(new_student, "that ok")