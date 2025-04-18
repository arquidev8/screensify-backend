from typing import Any, Dict, List
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.screen import Screen
from app.schemas.screen import ScreenCreate, ScreenUpdate

class CRUDScreen(CRUDBase[Screen, ScreenCreate, ScreenUpdate]):
    def create(self, db: Session, *, obj_in: ScreenCreate) -> Screen:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Screen(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_project(self, db: Session, *, project_id: int, skip: int = 0, limit: int = 100) -> List[Screen]:
        """Get multiple screens for a project"""
        return db.query(self.model).filter(self.model.project_id == project_id).offset(skip).limit(limit).all()

screen = CRUDScreen(Screen)
