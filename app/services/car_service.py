from app.repositories.car import CarRepository
from app.models.car import Car

class CarService:
    def __init__(self, db):
        self.repo = CarRepository(db)

    def create_car(self, brand, model, year, price_per_day):
        car = Car(brand=brand, model=model, year=year, price_per_day=price_per_day)
        return self.repo.create(car)

    def get_all_cars(self):
        return self.repo.get_all()

    def update_status(self, car_id, status):
        return self.repo.update_status(car_id, status)
