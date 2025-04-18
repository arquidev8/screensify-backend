from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps

router = APIRouter(prefix="/componentinstances", tags=["componentinstances"])

@router.post("/", response_model=schemas.component_instance.ComponentInstance)
@router.post("", response_model=schemas.component_instance.ComponentInstance)
def create_component_instance(
    *,
    db: Session = Depends(deps.get_db),
    ci_in: schemas.component_instance.ComponentInstanceCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    # verify screen belongs to user
    screen = crud.screen.get(db, id=ci_in.screen_id)
    if not screen or screen.project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Screen not found or unauthorized")
    ci = crud.componentinstance.create(db, obj_in=ci_in)
    return ci

@router.get("/", response_model=List[schemas.component_instance.ComponentInstance])
@router.get("", response_model=List[schemas.component_instance.ComponentInstance])
def read_component_instances(
    screen_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    screen = crud.screen.get(db, id=screen_id)
    if not screen or screen.project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Screen not found or unauthorized")
    return crud.componentinstance.get_multi_by_screen(db, screen_id=screen_id, skip=skip, limit=limit)

@router.put("/{ci_id}", response_model=schemas.component_instance.ComponentInstance)
def update_component_instance(
    ci_id: int,
    *,
    db: Session = Depends(deps.get_db),
    ci_in: schemas.component_instance.ComponentInstanceUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    ci = crud.componentinstance.get(db, id=ci_id)
    if not ci or ci.screen.project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="ComponentInstance not found or unauthorized")
    return crud.componentinstance.update(db, db_obj=ci, obj_in=ci_in)

@router.delete("/{ci_id}", response_model=schemas.component_instance.ComponentInstance)
def delete_component_instance(
    ci_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    ci = crud.componentinstance.get(db, id=ci_id)
    if not ci or ci.screen.project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="ComponentInstance not found or unauthorized")
    return crud.componentinstance.remove(db, id=ci_id)
