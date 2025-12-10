from pydantic import BaseModel, ConfigDict
from typing import Optional

class CarCreate(BaseModel):
    brand: str
    model: str
    year: int
    price_per_day: float

class CarOut(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    price_per_day: float
    status: str

    model_config = ConfigDict(from_attributes=True)
