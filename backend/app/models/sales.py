from datetime import date

from database import Base
from models.books import Book
from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey, Integer,
                        SmallInteger, String, Text)



class Sales(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey(Book.id), nullable=True)
    quantity = Column(Integer, nullable=False,)
    
    def __init__(self, book_id: int, quantity: int):
        self.book_id = book_id
        self.quantity = quantity

        
    def toDict(self):
        return{
            'id': self.id,
            'book_id': self.name,
            'quantity': self.price,
        }