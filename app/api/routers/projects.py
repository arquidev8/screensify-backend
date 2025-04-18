from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/", response_model=schemas.project.Project)

def create_project(*, db: Session = Depends(deps.get_db), project_in: schemas.project.ProjectCreate,
                   current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    # Check duplicate name
    existing = crud.project.get_multi_by_owner(db, owner_id=current_user.id, skip=0, limit=1)
    if any(p.name == project_in.name for p in existing):
        raise HTTPException(status_code=400, detail="Ya existe un proyecto con ese nombre")
    project = crud.project.create(db, obj_in=project_in, owner_id=current_user.id)
    return project


@router.get("/", response_model=List[schemas.project.Project])
def read_projects(db: Session = Depends(deps.get_db),
                  skip: int = 0, limit: int = 100,
                  current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    projects = crud.project.get_multi_by_owner(db, owner_id=current_user.id, skip=skip, limit=limit)
    return projects

