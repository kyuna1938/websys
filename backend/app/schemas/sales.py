from pydantic import BaseModel

class CreateSales(BaseModel):
    book_id: int
    quantity: int

class Sales(CreateSales):
    id: int

    class Config:
        orm_mode = True
