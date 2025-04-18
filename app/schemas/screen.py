from typing import Optional, Any
from pydantic import BaseModel


class ScreenBase(BaseModel):
    name: str
    description: Optional[str] = None
    project_id: int
    layout_data: Optional[Any] = None
    code_data: Optional[Any] = None
    order: Optional[int] = 0
    is_active: Optional[bool] = True


class ScreenCreate(ScreenBase):
    pass


class ScreenUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    layout_data: Optional[Any] = None
    code_data: Optional[Any] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None


class Screen(ScreenBase):
    id: int

    class Config:
        orm_mode = True
