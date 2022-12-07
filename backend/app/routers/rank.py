from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, desc, func
from datetime import datetime, date
from typing import Any

router = APIRouter(
    prefix="/ranks",
    tags=["ranks"],
    responses={404: {"description": "Not found"}},
)



import models.sales
import models.books
import schemas.sales
import dependencies

@router.get("")
def get_ranks(
    start_date: date = None,
    end_date: date = None,
    db: Session = Depends(dependencies.get_db),
):
    if not (start_date and end_date):
        start_date = date.today()
        end_date = date.today()
    start = datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
    end = datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59)
    print(start)
    db_rank = db.query(models.sales.Sales.book_id, models.books.Book.name, func.sum(models.sales.Sales.quantity).label("quantity")).\
        join(models.sales.Sales, models.sales.Sales.book_id == models.books.Book.id).\
            filter(models.sales.Sales.date.between(start, end)).\
                group_by(models.sales.Sales.book_id).\
                    order_by(desc("quantity")).\
                        all()
    return db_rank


@router.post("")
def create_sales(
    create_sale: schemas.sales.CreateSales,
    db: Session = Depends(dependencies.get_db),
):
    db_sale = models.sales.Sales(
        book_id=create_sale.book_id,
        quantity=create_sale.quantity,
        date=create_sale.date,
        sex=create_sale.sex,
    )
    db.add(db_sale)
    db.flush()
    db.commit()
    return {"message": "succses"}

@router.get("/{id}")
def get_gender_ratio(
    id: int,
    db: Session = Depends(dependencies.get_db),
):
    db_books = db.query(models.sales.Sales).filter(models.sales.Sales.book_id == id).all()
    db_name = db.query(models.books.Book).filter(models.books.Book.id == id).first()
    raito: dict[str, Any] = dict()
    raito['name'] = db_name.name
    raito['man'] = 0
    raito['woman'] = 0
    raito['other'] = 0
    for db_book in db_books:
        if db_book.sex == 0:
            raito['man'] = raito['man'] + db_book.quantity
        elif db_book.sex == 1:
            raito['woman'] = raito['woman'] + db_book.quantity
        elif db_book.sex == 2:
            raito['other'] = raito['other'] + db_book.quantity

    return raito