from fastapi import FastAPI
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
import json
app = FastAPI()
class Data(BaseModel):
    user: str

class Question(BaseModel):
    category: str
    question: str
    timestamp: str
    description: Optional[str] = None
    steps: List[str]

@app.get("/cate/{cate_name}/q/{q_num}")
async def root(cate_name: str, q_num: str):
    with open("data.json",'r') as f:
        data = json.load(f)
    json_compatible_item_data = jsonable_encoder(data[q_num])
    return JSONResponse(content=json_compatible_item_data)

# @app.post("/q/{q_num}",response_model=Question)
@app.post("/q/{q_num}")
def gene_question(q_num:str, question:Question):
    with open("data.json",'r') as f:
        data = json.load(f)
    data[q_num] = jsonable_encoder(question)
    print(data)
    with open("data.json",'w') as f:
        json.dump(data, f)
    return "OK"
