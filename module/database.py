from pymongo import MongoClient
import os

# เก็บเอาไว้กันลืม
client =  MongoClient(os.getenv("MONGO_URL"))
# client =  MongoClient("mongodb+srv://promtgov:promtgov@cluster0.b1xky3c.mongodb.net/")#รอเชื่อมกับฐานข้อมูล จริงๆต้องเชื่อมกับฐานข้อมูลที่อยู่บนเซิฟเวอร์

db = client['mongo-db']
users_collection = db["users"]