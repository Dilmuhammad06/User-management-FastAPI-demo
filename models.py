from pydantic import BaseModel

class Notes(BaseModel):
    text:str
    author:str

class User(BaseModel):
    name:str