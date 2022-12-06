from fastapi import Response, status, APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, asc

router = APIRouter(
    prefix="/ranks",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)



import models.sales
import dependencies

@router.get()
def get_ranks(
    db: Session = Depends(dependencies.get_db)
):
    db_rank = db.query(models.sales.Sales).order_by(asc(models.sales.quantity))
    return db_rank


@router.post()
def create_sales(
    db: Session = Depends(dependencies.get_db) 
):
    return{"b"}