from sqlalchemy.orm import Session
from app.models.car import Car

class CarRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, car: Car):
        self.db.add(car)
        self.db.commit()
        self.db.refresh(car)
        return car

    def get_all(self):
        return self.db.query(Car).all()

    def get_by_id(self, car_id: int):
        return self.db.query(Car).filter(Car.id == car_id).first()

    def update_status(self, car_id: int, status: str):
        car = self.get_by_id(car_id)
        if car:
            car.status = status
            self.db.commit()
            self.db.refresh(car)
        return car
