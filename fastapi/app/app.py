import string
from fastapi import FastAPI
from chatbot.train import train_model

app = FastAPI()

@app.post("/getReply", tags=['ChatBot'])
async def getReply(question:dict)->list:
    print(question)
    return ["Thank you for asking the question"]

@app.get("/trainModel", tags=['Chatbot'])
async def trainModel()->str:
    train_model()