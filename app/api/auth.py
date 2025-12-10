from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.services.auth import AuthService
from app.schemas.user import UserCreate, SUser


router = APIRouter(prefix="/auth")

@router.post("/register", response_model=SUser)
def register(data: UserCreate, db: Session = Depends(get_db)):
    service = AuthService(db)
    user = service.create_user(data.username, data.password)
    return SUser(id=user.id, username=user.username)


@router.post("/login")
def login(data: UserCreate, db: Session = Depends(get_db)):
    service = AuthService(db)
    return {"user_id": service.login(data.username, data.password)}

