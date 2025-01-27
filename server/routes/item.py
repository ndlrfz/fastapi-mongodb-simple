from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_item,
    get_items,
    get_item,
    delete_item,
    change_item,
)

from server.models.itemModels import (
    Item,
    ItemUpdate,
)

router = APIRouter()

# add new item operation
@router.post("/")
async def add_item_data(item: Item = Body(...)):
    item = jsonable_encoder(item)
    new_item = await add_item(item)
    return new_item

# get all available items
@router.get("/")
async def get_item_data():
    items = await get_items()
    if items:
        return items
    return "No available item."

# show detailed of item via id
@router.get("/{id}")
async def get_item_details(id):
    item_details = await get_item(id)
    if item_details:
        return item_details
    return "Item not found."

# Update Item
@router.put("/{id}")
async def update_item(id: str, data: ItemUpdate = Body(...)):
    data = {k: v for k, v in data.dict().items() if v is not None}
    updated_item = await change_item(id, data)
    if updated_item:
        return{f'Success: item {id} updated.'}
    return "Error"

# delete item via id
@router.delete("/{id}")
async def remove_item(id: str):
    item_to_delete = await delete_item(id)
    if item_to_delete:
        return item_to_delete
    return{f'Item {id} Not Available.'}

