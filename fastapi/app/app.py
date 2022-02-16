import string
from fastapi import FastAPI

app = FastAPI()

@app.post("/getReply", tags=['ChatBot'])
async def getReply(question:dict)->list:
    print(question)
    return ["Thank you for asking the question"]