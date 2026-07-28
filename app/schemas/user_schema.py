from pydantic import BaseModel, Field

class UserRegisterRequest(BaseModel):
    username: str = Field(..., min_length=4)
    password: str = Field(..., min_length=4)

#particullar user registered successfully. Below class hoda username with string as type
class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True

class UserUpdateRequest(BaseModel):
    username: str | None = Field(
        default=None,
        min_length=4
    ) 


