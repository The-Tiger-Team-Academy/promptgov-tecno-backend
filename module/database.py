from pymongo import MongoClient
import os

# เก็บเอาไว้กันลืม
client =  MongoClient(os.getenv("MONGO_URL"))

db = client['example']
users_collection = db["users"]

