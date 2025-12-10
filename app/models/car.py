from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String)
    year = Column(Integer)
    price_per_day = Column(Float)
    status = Column(String, default="available")
