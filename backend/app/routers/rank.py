from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, desc, func
from datetime import datetime, date

router = APIRouter(
    prefix="/ranks",
    tags=["ranks"],
    responses={404: {"description": "Not found"}},
)



import models.sales
import models.books
import schemas.sales
import dependencies

@router.get("/")
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


@router.post("/")
def create_sales(
    create_sale: schemas.sales.CreateSales,
    db: Session = Depends(dependencies.get_db),
):
    db_sale = models.sales.Sales(
        book_id=create_sale.book_id,
        quantity=create_sale.quantity,
        date=create_sale.date
    )
    db.add(db_sale)
    db.flush()
    db.commit()
    return {"message": "succses"}