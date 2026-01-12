from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    id: int

class UserModel:
    email: str
    name: str
    id: int

    def __init__(self, name: str, email: str, id: int):
        self.name = name
        self.email = email
        self.id = id

