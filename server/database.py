from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId

from server.models.itemModels import (
    Item,
    ItemUpdate,
)

MONGODB_HOST = "mongodb://localhost:27017"

connection = AsyncIOMotorClient(MONGODB_HOST)

database = connection.items
item_collection = database.get_collection("item_collection")

def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "category": item["category"],
        "stocks": item["stocks"],
        "price": item["price"],
    }

# add new item
async def add_item(item_details: dict) -> dict :
    item = await item_collection.insert_one(item_details)
    new_item = await item_collection.find_one({"_id": item.inserted_id})
    return item_helper(new_item)

# retrieve all items
async def get_items():
    items = []
    async for item in item_collection.find():
        items.append(item_helper(item))
    return items

# retrieve specific item
async def get_item(id: str) -> dict:
    item = await item_collection.find_one({"_id": ObjectId(id)})
    if item:
        return item_helper(item)
    return "Item Not Found."

# update item
async def change_item(id: str, data: dict):
    if len(data) < 1:
        return "Please input your data"
    find_item = await item_collection.find_one({"_id": ObjectId(id)})
    if find_item:
        item_update = await item_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        if item_update:
            return True
        return False

# delete an item
async def delete_item(id: str):
    item = await item_collection.find_one({"_id": ObjectId(id)})
    if item:
        await item_collection.delete_one({"_id": ObjectId(id)})
        return(f'Item {id} deleted.')
    return "Item Not Found."
