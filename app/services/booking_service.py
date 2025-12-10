from app.repositories.booking import BookingRepository
from app.models.booking import Booking

class BookingService:
    def __init__(self, db):
        self.repo = BookingRepository(db)

    def book_car(self, user_id, car_id, start_date, end_date):
        if not self.repo.check_availability(car_id, start_date, end_date):
            raise Exception("Car is not available for these dates")
        booking = Booking(user_id=user_id, car_id=car_id, start_date=start_date, end_date=end_date)
        return self.repo.create(booking)

    def user_bookings(self, user_id):
        return self.repo.get_user_bookings(user_id)

    def all_bookings(self):
        return self.repo.get_all()
