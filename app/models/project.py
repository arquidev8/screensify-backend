from typing import List, Optional

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Project(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    target_environment = Column(String, index=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    is_active = Column(Boolean(), default=True)
    
    # Relaciones
    owner = relationship("User", back_populates="projects")
    screens = relationship("Screen", back_populates="project", cascade="all, delete-orphan")