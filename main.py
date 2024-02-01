from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from services import generate_message_record, post_user, save_payment, create_doc_messagerecord, messageRecordfordownload, store_url, get_url

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(save_payment.router)
app.include_router(generate_message_record.router)
app.include_router(create_doc_messagerecord.router)
app.include_router(post_user.router)
app.include_router(messageRecordfordownload.router)
app.include_router(store_url.router)
app.include_router(get_url.router)
# app.include_router(uploadToStorage.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
