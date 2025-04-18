from typing import Optional, Any
from pydantic import BaseModel


class ComponentInstanceBase(BaseModel):
    screen_id: int
    component_type: str
    props: Optional[Any] = None
    parent_id: Optional[int] = None
    order: Optional[int] = 0
    is_active: Optional[bool] = True


class ComponentInstanceCreate(ComponentInstanceBase):
    pass


class ComponentInstanceUpdate(BaseModel):
    component_type: Optional[str] = None
    props: Optional[Any] = None
    parent_id: Optional[int] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None


class ComponentInstance(ComponentInstanceBase):
    id: int

    class Config:
        orm_mode = True
