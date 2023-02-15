from fastapi import APIRouter, HTTPException, status, Body
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder

from bson import ObjectId

from ecommerce.db import inventories as inventories_collection
from ecommerce.inventory.models import Inventory
from ecommerce.inventory.schemas import inventories_serializer, inventory_serializer

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/")
async def list_inventories():
    result = await inventories_collection.find().to_list(1000)
    inventories = inventories_serializer(result)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=inventories)


@router.post("/")
async def add_new_inventory(model: Inventory):
    inventory = jsonable_encoder(model)
    new_inventory = await inventories_collection.insert_one(inventory)
    created_inventory = await inventories_collection.find_one({"_id": new_inventory.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=inventory_serializer(created_inventory))


@router.put("/{id}")
async def update_inventory(id: str, model: Inventory = Body()):
    inventory = jsonable_encoder(model)
    _id = ObjectId(id)
    update_inventory = await inventories_collection.update_one({"_id": _id}, {"$set": inventory})
    if update_inventory.modified_count == 1:
        updated_inventory = await inventories_collection.find_one({"_id": _id})
        if updated_inventory is not None:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content=inventory_serializer(updated_inventory))
    return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"inventory {id} do not be update")

    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"inventory {id} do not be update")


@router.get("/{id}")
async def get_inventory(id: str):
    inventory = await inventories_collection.find_one({"_id": ObjectId(id)})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=inventory_serializer(inventory))


@router.delete("/{id}")
async def delete_inventory(id: str):
    result = await inventories_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Student {id} not found")
