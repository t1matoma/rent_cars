from app.repositories.booking import BookingRepository
from app.models.booking import Booking
from app.models.car import Car
from fastapi import HTTPException

class BookingService:
    def __init__(self, db):
        self.repo = BookingRepository(db)
        self.db = db

    def book_car(self, user_id, car_id, start_date, end_date):
        # Проверка машины
        car = self.db.query(Car).filter(Car.id == car_id).first()
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")

        booking = Booking(
            user_id=user_id,
            car_id=car_id,
            start_date=start_date,
            end_date=end_date,
            status="active"
        )

        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return booking


    def user_bookings(self, user_id):
        return self.repo.get_user_bookings(user_id)

    def all_bookings(self):
        return self.repo.get_all()
