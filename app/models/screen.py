from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, JSON
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Screen(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)
    layout_data = Column(JSON, nullable=True)  # Almacena la estructura de componentes
    code_data = Column(JSON, nullable=True)    # Almacena código personalizado
    order = Column(Integer, default=0)         # Orden de la pantalla en el proyecto
    is_active = Column(Boolean(), default=True)
    
    # Relaciones
    project = relationship("Project", back_populates="screens")