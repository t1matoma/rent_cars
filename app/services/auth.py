from app.repositories.user import UserRepository

from sqlalchemy.orm import Session

import bcrypt

from fastapi import HTTPException


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = UserRepository(db)
    
    
    def create_user(self, username: str, password: str):
        if self.repo.get_by_username(username):
            raise HTTPException(status_code=409, detail="Username is already taken")
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return self.repo.create(username, hashed_password.decode("utf-8"))

    
    def login(self, username: str, password: str):
        user = self.repo.get_by_username(username)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return user.id