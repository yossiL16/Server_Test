import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



def load_data():
    with open("names.txt", "r") as f:
        file_name = f.read()
        return file_name

def save_data(name):
    with open("names.txt", "w") as f:
        f.write(name)

app = FastAPI()

class Caesar(BaseModel):
    text:str
    offest:int
    mood:str

@app.get("/test")
def test():
    return {"msg":"hi from test"}

@app.get("/test/")
def saved_name(name):
    try:
        text = str(load_data())
        text += name
        save_data(text)
    except:
        return







@app.post("/Caesar/")
def Caesar_cipher(item:Caesar):
    if item.mood == "encrypt":
        text = item.text


