from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse, Response

from ecommerce.customer.models import CustomerPost, Customer
from ecommerce.customer.schemas import customer_serializer, customers_serializer
from ecommerce.db import customers as customers_collection

router = APIRouter(prefix="/customer", tags=["Customer"])


@router.get("/")
async def list_customers():
    customers = await customers_collection.find().to_list(100)
    return JSONResponse(status_code=status.HTTP_200_OK, content=customers_serializer(customers))


@router.get("/{email}")
async def list_customers(email: str):
    customer = await customers_collection.find_one({"_id": email})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=customer_serializer(customer))


@router.post("/")
async def add_new_customer(model: CustomerPost = Body()):
    customer = jsonable_encoder(model, exclude=["email"])
    customer["_id"] = model.email
    new_customer = await customers_collection.insert_one(customer)
    created_customer = await customers_collection.find_one({"_id": new_customer.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=customer_serializer(created_customer))


@router.put("/{email}")
async def update_customer(email: str, model: Customer = Body()):
    customer_encoder = jsonable_encoder(model, exclude=["email"])
    update_customer = await customers_collection.update_one({"_id": email}, {"$set": customer_encoder} )
    if update_customer.modified_count == 1:
        updated_customer = await customers_collection.find_one({"_id": email})
        if updated_customer is not None:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content=customer_serializer(updated_customer))
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"inventory {id} do not be update")


@router.delete("/{email}")
async def delete_customer(email: str):
    result = await customers_collection.delete_one({"_id": email})
    if result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Student {id} not found")