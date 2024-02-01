from module.database import users_collection
from fastapi import APIRouter
from entity.users import Users

router = APIRouter(
    tags=["Create_user Services"],
    responses={
        404:{"discription": "NOT FOUND!!"}
    },
    
)

@router.post("/Users")
async def create_users(Users: Users):
    # Check if an entry with the same email already exists
    existing_Users = users_collection.find_one({"email": Users.email})
    
    # If an entry exists, return an appropriate response
    # If an entry exists, return an appropriate response
    if existing_Users:
        return {"id": str(existing_Users.get('_id', None))}

    # If no entry exists, insert the new Users
    result = users_collection.insert_one(Users.dict())
    return {"name": Users.name, "email": Users.email, "img": Users.img, "id": str(result.inserted_id)}