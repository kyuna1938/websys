from pydantic import BaseModel

class CreateBook(BaseModel):
    name: str
    price: int

class Book(CreateBook):
    id: int

    class Config:
        orm_mode = True
