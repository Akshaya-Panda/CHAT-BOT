import string
from fastapi import FastAPI
from chatbot.train import train_model
from chatbot.chat import get_reply

app = FastAPI()

@app.post("/getReply", tags=['ChatBot'])
async def getReply(question:dict)->list:
    return [get_reply(question['question'])]

@app.get("/trainModel", tags=['Chatbot'])
async def trainModel()->str:
    return train_model()