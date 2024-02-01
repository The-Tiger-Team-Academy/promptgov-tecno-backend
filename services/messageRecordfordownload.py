from docx import Document
from fastapi.responses import FileResponse
from fastapi import APIRouter
from io import BytesIO

router = APIRouter(
    tags=["Download Services"],
    responses={
        404:{"discription": "NOT FOUND!!"}
    },
    
)

#TODO: #12 Refactor this function
@router.get("/download/messageRecord/")
async def messageRecordfordownload():

    doc = Document('./templatedoc/messageRecordfordownload.docx')
    
    new_doc = BytesIO()
    doc.save(new_doc)
    new_doc.seek(0)

    temp_file_path = "/tmp/generated.docx"
    with open(temp_file_path, "wb") as tmp_file:
        tmp_file.write(new_doc.getvalue())

    return FileResponse(temp_file_path, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document', filename="generated.docx")
