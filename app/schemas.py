from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Optional
from enum import Enum

class Gender(str, Enum):
    male = 'M'
    female = 'F'

class UserBase(BaseModel):
    name: str
    age: int = Field(..., ge=0, description="Age must be a non-negative integer")
    gender: Gender
    email: EmailStr
    city: str
    interests: List[str]

    @field_validator('email')
    def email_validator(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, description="Age must be a non-negative integer")
    gender: Optional[Gender] = None
    email: Optional[EmailStr] = None
    city: Optional[str] = None
    interests: Optional[List[str]] = None

    @field_validator('email')
    def email_validator(cls, v):
        if v and '@' not in v:
            raise ValueError('Invalid email address')
        return v

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
