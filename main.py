import json
from operator import index

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
    latters = ["a", "b", "c", "d", "e","f","g","h", "i","j","k","l","m","n","o","p","q","r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_sentens = []
    if item.mood == "encrypt":
        texti = item.text.replace(" ", "")
        for i, in texti:
            for j in latters:
                if i == j:
                    new_sentens.append(new_sentens[(index(j) + item.offest) % 26])
        return {"encrypted_text":str(new_sentens)}

    elif item.mood == "decrypt":
        texti = item.text.replace(" ", "")
        for i, in texti:
            for j in latters:
                if i == j:
                    new_sentens.append(new_sentens[(index(j) - item.offest) % 26])
        return {"decrypted_text": str(new_sentens)}
    else:
        return "error"

@app.get("/texts/{text}")
def Encryption(text):
    regular_text = text.replace(" ", "")
    for i in range(regular_text):
        l = ""
        r = ""
        if i % 2 == 0:
            l += regular_text[i]
        else:
            r += regular_text[i]
        l += r
        return { "encrypted_text": l }


class Fence(BaseModel):
    text:str
@app.post("/decrypt/")
def decrypt(text:Fence):
    l = ""
    r = ""
    midel= len(text.text) // 2
    l += text.text[ : midel]
    r += text.text[midel: ]

    l += r
    return { "decrypted": l}


