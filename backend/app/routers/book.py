from fastapi import Response, status, APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, asc

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)

import models.books
import schemas.books
import dependencies

@router.get("")
def get_books(
    db: Session = Depends(dependencies.get_db),
):
    db_book = db.query(models.books.Book).all()
    return db_book

@router.post("")
def create_book(
    create_book: schemas.books.CreateBook,
    db: Session = Depends(dependencies.get_db),   
):
    db_book = models.books.Book(
        name=create_book.name,
        price=create_book.price,
    )
    db.add(db_book)
    db.flush()
    db.commit()
    return {"message": "succses"}

@router.get("/{id}")
def get_book_by_id(
    id: int,
    db: Session = Depends(dependencies.get_db),  
):
    db_book = db.query(models.books.Book).filter(models.books.Book.id == id).first()
    return db_book