from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str = Field(..., min_length=4)
    password: str = Field(..., min_length=4)
    
