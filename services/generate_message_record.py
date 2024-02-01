import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os

from dotenv import load_dotenv

load_dotenv()

def generate_message(message: str):
    chat = ChatOpenAI(temperature=1, openai_api_key= os.environ.get('OPENAI_API_KEY', None))
    messagesWithPrompt = [
    SystemMessage(
        content='''
    You are a machine for creating MessageRecord (บันทึกข้อความ) in the Thai language (MessageRecord is a Thai Document that represents official messages between agencies or departments)

example1 messageRecord about Invitation people:
ตามที่  เทศบาลเมืองอุทัยธานี ขอเชิญข้าพเจ้า นายชลาวัฒน์  ชลมาก  เป็นวิทยากรให้ความรู้แก่เด็กและเยาวชน ที่เข้าร่วมโครงการส่งเสริมและสนับสนุนกิจกรรมพัฒนาเด็กและเยาวชนเทศบาลเมืองอุทัยธานี  ในกิจกรรมนันทนาการ โดยนายบัญชา เสมากูล  เป็นผู้นำดำเนินรายการ ในวันศุกร์ที่  18  พฤษภาคม  2561  เวลา  09.00 – 10.00  น.  ณ  แพบวชน้ำ วัดอุโบสถาราม  จังหวัดอุทัยธานี  นั้น 
ข้าพเจ้า จึงขออนุญาตไปเป็นวิทยาการ  ในวัน  เวลา  และสถานที่ดังกล่าว  ทั้งนี้  ข้าพเจ้า ไม่มีชั่วโมงสอนในช่วงคาบเรียนที่  1 – 3  (เวลา  08.30 – 11.00  น.)

example2 messageRecord about showing department budget:
ตำมหนังสือกรมกำรพัฒนำชุมชน ที่ มท 0403.2/ว 2044 ลงวันที่ 6 ตุลำคม 2560
เรื่อง กำรโอนจัดสรรงบประมำณค่ำใช้จ่ำยในกำรบริหำร ประจ ำปีงบประมำณ พ.ศ. 2561 ส ำหรับไตรมำสที่
1-2 (ตุลำคม 2560 – มีนำคม 2561) ได้โอนจัดสรรงบประมำณ งบด ำเนินงำน ค่ำใช้จ่ำยในกำรบริหำร
รำยกำรค่ำตอบแทน ใช้สอยและวัสดุ ประจ ำปีงบประมำณ พ.ศ. 2561 จ ำนวน 2,031,100 บำท
(สองล้ำนสำมหมื่นหนึ่งพันหนึ่งร้อยบำทถ้วน)

example3 messageRecord about Borrow something from department:
ตามที่ สำนักงานสาธารณสุขธารณสุขจังหวัดกำแพงเพชร ได้ดำเนินการการจัดทำแนวทาง
ปฏิบัติเกี่ยวกับการใช้ทรัพย์สินของราชการที่ถูกต้อง ให้หน่วยงานได้ยึดถือปฏิบัติ ตามโครงการประเมิน
คุณธรรม และความโปร่งใสในการดำเนินงานของหน่วยงานภาครัฐ ( Integrity and Transparency
Assessment : ITA) ประจำปีงบประมาณ พ.ศ. ๒๕๖๔ หน่วยงานในสังกัดกระทรวงสาธารณสุขผ่านเกณฑ์การ
ประเมิน ITA (ร้อยละ ๙๒) ซึ่งเป็นการประเมินเพื่อวัดระดับคุณธรรมและความโปร่งใสในการดำเนินงานของ
หน่วยงาน นั้น
 ในการนี้ สำนักงานสาธารณสุขอำเภอทรายทองวัฒนา ได้ส่งแนวปฏิบัติเกี่ยวกับการยืม
พัสดุประเภทใช้คงรูประหว่างหน่วยงานของรัฐ ยืมใช้ภายในสถานที่ของหน่วยงานของรัฐเดียวกัน และการ
ยืมไปใช้นอกสถานที่ของหน่วยงานของรัฐ ให้หน่วยงานในสังกัดรับทราบและยึดถือปฏิบัติ และขออนุญาต
เผยแพร่ผ่านเว็บไซต์สำนักงานสาธารณสุขอำเภอทรายทองวัฒนา (ช่องทางประชาสัมพันธ์กิจกรรม ITA) และ
ช่องทางประชาสัมพันธ์ต่างๆ

Please create a draft of the message record when a user inputs a few keywords or storyline:

if the user missing information please create a message record based on your thoughts.
    '''
    ),
    HumanMessage(
        content=message
    ),
]

    result = chat(messagesWithPrompt)
    return result

class Message(BaseModel):
    content: str



router = APIRouter(
    tags=["Gennerate Services"],
    responses={
        404:{"discription": "NOT FOUND!!"}
    },
    
)

@router.post("/gennrate_message_record")
def save_payment(message: Message):
    # payment_dict = payment.model_dump();
    result = generate_message(message.content)
    
    return {"message": result}
    # if result.inserted_id:
    #     return {"message": "Payment saved successfully", "id": str(result.inserted_id)}
    # else:
    #     raise HTTPException(status_code=500, detail="Failed to save payment")