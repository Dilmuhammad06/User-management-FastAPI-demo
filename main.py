from fastapi import FastAPI
from datetime import datetime
import random
from models import Notes, User

app = FastAPI()

splashes = [
    "Hello dear user",
    "Happy to see you again",
    "Wassup my nigga",
    "I know you love KFC!",
    "Color doesn't matter, but in America"
]


@app.get('/')
async def index():
    rand = random.randint(0,4)
    data = {
        "page":"Index",
        "splash":splashes[rand],
        "company":"Dizen",
        "year":str(datetime.now().year)
    }
    return data

users = {
    1:"Dilmuhammad",
    2:"Murodjon",
    3:"Boburjon",
    4:"Azamjon",
    5:"Ikromjon"
}

@app.get('/users')
async def list_users():
    return users


@app.get('/get_user/{user_id}')
async def get_user(user_id:int):
    for key,value in users.items():
        if key == user_id:
            return {"id":user_id,"name":value}
    return {"msg":"not found 404"}

@app.post('/create_note/')
async def create_note(note:Notes):
    print(note.author)
    return note

@app.delete('/delete_user/{user_id}')
async def delete_user(user_id:int):
    for key,value in users.items():
        if key == user_id:
            del users[user_id]
            return users
    return {"status":False,"msg":"User not found 404 :("}

@app.post('/add_user')
async def add_user(user:User):
    rand = random.randint(1,111)
    users.update({rand:user.name})
    return users