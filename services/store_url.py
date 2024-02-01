from fastapi import APIRouter, HTTPException
from module.database import users_collection
from entity.users import UserURLHistory

router = APIRouter(
    tags=["StoreUrl Services"],
    responses={404: {"description": "Not found"}}
)

@router.post("/store_url/")
async def store_url(data: UserURLHistory):
    user_id = data.user_id
    urls_data = [url_item.dict() for url_item in data.urls]
    existing_user = users_collection.find_one({"user_id": user_id})

    if existing_user:
        users_collection.update_one(
            {"user_id": user_id},
            {"$push": {"urls": {"$each": urls_data}}}
        )
    else:
        user_data = data.dict()
        user_data["urls"] = urls_data
        users_collection.insert_one(user_data)

    return {"message": "URLs stored successfully"}


