from pydantic import BaseModel, Field

class UserRegisterRequest(BaseModel):
    username: str = Field(..., min_length=4)
    password: str = Field(..., min_length=4)

#particullar user registered successfully. Below class hoda username with string as type
class UserResponse(BaseModel):
    username: str 

