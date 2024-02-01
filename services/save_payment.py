from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from module.database import db

class SavePayment(BaseModel):
    userid: str
    documentId: str
    stripeId: str
    docType: str
    price: int

router = APIRouter(
    tags=["User Services"],
    responses={
        404:{"discription": "NOT FOUND!!"}
    },
    
)

payments_collection = db["payments"]
users = db["users"]

@router.post("/save_payment")
def save_payment(payment: SavePayment):
    payment_dict = payment.model_dump();
    cursor = users.find()
    for record in cursor:
        if str(record['_id']) == payment.userid:
             result = payments_collection.insert_one(payment_dict)
             break
        else:
            raise HTTPException(status_code=404, detail="User not found")
    

    
    if result.inserted_id:
        return {"message": "Payment saved successfully", "id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to save payment")


    