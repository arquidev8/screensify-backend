from typing import Any, Dict, List, Union
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.component_instance import ComponentInstance
from app.schemas.component_instance import ComponentInstanceCreate, ComponentInstanceUpdate

class CRUDComponentInstance(CRUDBase[ComponentInstance, ComponentInstanceCreate, ComponentInstanceUpdate]):
    def get_multi_by_screen(self, db: Session, *, screen_id: int, skip: int = 0, limit: int = 100) -> List[ComponentInstance]:
        """Get all component instances for a given screen"""
        return db.query(self.model).filter(self.model.screen_id == screen_id).offset(skip).limit(limit).all()

componentinstance = CRUDComponentInstance(ComponentInstance)
