from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.booking import Booking

class BookingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, booking: Booking):
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return booking

    def check_availability(self, car_id: int, start_date, end_date):
        conflict = self.db.query(Booking).filter(
            Booking.car_id == car_id,
            Booking.status == "active",
            Booking.start_date <= end_date,
            Booking.end_date >= start_date
        ).first()
        return conflict is None

    def get_user_bookings(self, user_id: int):
        return self.db.query(Booking).filter(Booking.user_id == user_id).all()

    def get_all(self):
        return self.db.query(Booking).all()
