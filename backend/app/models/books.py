
from database import Base
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import relationship



class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False, index=True)
    price = Column(Integer, nullable=False,)
    
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

        
    def toDict(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price,
        }