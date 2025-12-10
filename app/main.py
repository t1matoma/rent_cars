from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.database import engine, Base
from app.api import auth, cars, bookings

Base.metadata.create_all(bind=engine)

settings = get_settings()

app = FastAPI(title="Rent cars")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(cars.router)
app.include_router(bookings.router)

@app.get("/")
def home():
    return {"message": "Rent cars", "docs": "/docs"}

