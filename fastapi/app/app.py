import string
from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot.train import train_model
from chatbot.chat import get_reply

app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/getReply/{question}", tags=['ChatBot'])
async def getReply(question:str)->list:
    return get_reply(question)

@app.get("/trainModel", tags=['Chatbot'])
async def trainModel()->str:
    return train_model()