from fastapi import Response, status, APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, asc

router = APIRouter(
    prefix="/ranks",
    tags=["ranks"],
    responses={404: {"description": "Not found"}},
)



import models.sales
import schemas.sales
import dependencies

@router.get("/")
def get_ranks(
    db: Session = Depends(dependencies.get_db),
):
    db_rank = db.query(models.sales.Sales).order_by(asc(models.sales.quantity))
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