from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.car_service import CarService
from app.schemas.car import CarCreate, CarOut

router = APIRouter(prefix="/cars")

@router.post("/", response_model=CarOut)
def create_car(data: CarCreate, db: Session = Depends(get_db)):
    service = CarService(db)
    return service.create_car(data.brand, data.model, data.year, data.price_per_day)

@router.get("/", response_model=list[CarOut])
def list_cars(db: Session = Depends(get_db)):
    service = CarService(db)
    return service.get_all_cars()
