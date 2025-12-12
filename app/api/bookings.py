from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.booking_service import BookingService
from app.schemas.booking import BookingCreate, BookingOut
from app.utils.dependencies import require_admin, get_current_user

router = APIRouter(prefix="/user")

@router.post("/{user_id}/book", response_model=BookingOut)
def book_car(user_id: int, data: BookingCreate, db: Session = Depends(get_db)):
    service = BookingService(db)
    return service.book_car(user_id, data.car_id, data.start_date, data.end_date)

@router.get("/{user_id}/bookings", response_model=list[BookingOut])
def user_bookings(user_id: int, db: Session = Depends(get_db)):
    service = BookingService(db)
    return service.user_bookings(user_id)

@router.get("/bookings/all", response_model=list[BookingOut])
def all_bookings(db: Session = Depends(get_db), admin = Depends(require_admin)):
    service = BookingService(db)
    return service.all_bookings()
