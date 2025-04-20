from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.api.code_exporter import generate_screen_code

router = APIRouter(prefix="/screens", tags=["screens"])


@router.post("/", response_model=schemas.Screen)
def create_screen(
    *,
    db: Session = Depends(deps.get_db),
    screen_in: schemas.ScreenCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    # Verificar que el proyecto existe y pertenece al usuario
    project = crud.project.get(db, id=screen_in.project_id)
    if not project or project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado o sin acceso")
    screen = crud.screen.create(db, obj_in=screen_in)
    return screen


@router.get("/", response_model=List[schemas.Screen])
def read_screens(
    project_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    project = crud.project.get(db, id=project_id)
    if not project or project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado o sin acceso")
    return crud.screen.get_multi_by_project(db, project_id=project_id, skip=skip, limit=limit)


@router.get("/{screen_id}", response_model=schemas.Screen)
def read_screen(
    screen_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    screen = crud.screen.get(db, id=screen_id)
    if not screen or screen.project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Pantalla no encontrada o sin acceso")
    return screen


@router.get("/{screen_id}/generated_code")
def get_generated_code(
    screen_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    # Verificar acceso
    screen = crud.screen.get(db, id=screen_id)
    if not screen or screen.project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Pantalla no encontrada o sin acceso")
    code = generate_screen_code(db, screen_id)
    return {"code": code}


@router.put("/{screen_id}", response_model=schemas.Screen)
def update_screen(
    screen_id: int,
    *,
    db: Session = Depends(deps.get_db),
    screen_in: schemas.ScreenUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    screen = crud.screen.get(db, id=screen_id)
    if not screen or screen.project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Pantalla no encontrada o sin acceso")
    updated = crud.screen.update(db, db_obj=screen, obj_in=screen_in)
    return updated


@router.delete("/{screen_id}", response_model=schemas.Screen)
def delete_screen(
    screen_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    screen = crud.screen.get(db, id=screen_id)
    if not screen or screen.project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Pantalla no encontrada o sin acceso")
    removed = crud.screen.remove(db, id=screen_id)
    return removed
