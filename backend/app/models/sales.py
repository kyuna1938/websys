from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp

from datetime import datetime
from database import Base
from models.books import Book
from sqlalchemy import (Column, ForeignKey, Integer)



class Sales(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey(Book.id), nullable=True)
    quantity = Column(Integer, nullable=False,)
    date = Column(Timestamp, nullable=False, server_default=current_timestamp())
    
    def __init__(self, book_id: int, quantity: int, date: datetime):
        self.book_id = book_id
        self.quantity = quantity
        self.date = date

        
    def toDict(self):
        return{
            'id': self.id,
            'book_id': self.name,
            'quantity': self.price,
        }