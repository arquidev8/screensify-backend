from typing import Optional
from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    target_environment: str
    is_active: Optional[bool] = True


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    target_environment: Optional[str] = None
    is_active: Optional[bool] = None


class Project(ProjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
