from pydantic import BaseModel, ConfigDict
from datetime import date

class BookingCreate(BaseModel):
    car_id: int
    start_date: date
    end_date: date

class BookingOut(BaseModel):
    id: int
    user_id: int
    car_id: int
    start_date: date
    end_date: date
    status: str

    model_config = ConfigDict(from_attributes=True)
