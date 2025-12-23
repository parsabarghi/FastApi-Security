from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str


class UserIn(UserBase):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    email: EmailStr

class UserUpdate(UserBase):
    email: EmailStr | None = None
    password: str | None = None
    name: str | None = None