from fastapi import APIRouter, HTTPException
from module.database import users_collection
from bson import json_util
import json

router = APIRouter(
    tags=["Get_url Services"],
    responses={404: {"description": "Not found"}}
)

@router.get("/history/{user_id}")
async def get_history(user_id: str):
    user_history = users_collection.find_one({"user_id": user_id}, {"_id": 0})  # Exclude the _id field
    if user_history:
        # Convert the MongoDB document to JSON
        user_history_json = json.loads(json_util.dumps(user_history))
        return user_history_json
    else:
        raise HTTPException(status_code=404, detail="User not found")
