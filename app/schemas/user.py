from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    username: str
    password: str
    
class SUser(BaseModel):
    id: int
    username: str
    role: str|None = None
    
    model_config = ConfigDict(from_attributes=True)