from pydantic import BaseModel
from typing import List, Optional

class Users(BaseModel):
    name: str
    email: str
    img: str

class URLItem(BaseModel):
    url: str
    government: str

class UserURLHistory(BaseModel):
    user_id: str
    urls: List[URLItem]
