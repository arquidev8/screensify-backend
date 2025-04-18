from typing import Any, Dict, List
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    def create(self, db: Session, *, obj_in: ProjectCreate, owner_id: int) -> Project:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Project(owner_id=owner_id, **obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100) -> List[Project]:
        """Get multiple projects belonging to an owner"""
        return db.query(self.model).filter(self.model.owner_id == owner_id).offset(skip).limit(limit).all()

project = CRUDProject(Project)
