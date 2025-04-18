from typing import Optional

from pydantic import BaseModel, EmailStr


# Propiedades compartidas
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Propiedades para crear un usuario
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Propiedades para actualizar un usuario
class UserUpdate(UserBase):
    password: Optional[str] = None


# Propiedades adicionales para devolver desde la API
class User(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True