from pydantic import BaseModel
from datetime import datetime

class CreateSales(BaseModel):
    book_id: int
    quantity: int
    date: datetime

class Sales(CreateSales):
    id: int

    class Config:
        orm_mode = True
