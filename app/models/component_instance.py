from typing import Any, Dict
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship, backref

from app.db.base_class import Base


class ComponentInstance(Base):
    id = Column(Integer, primary_key=True, index=True)
    screen_id = Column(Integer, ForeignKey("screen.id"), nullable=False)
    component_type = Column(String, index=True, nullable=False)
    props = Column(JSON, default=dict)
    parent_id = Column(Integer, ForeignKey("componentinstance.id"), nullable=True)
    order = Column(Integer, default=0)
    is_active = Column(Boolean(), default=True)

    screen = relationship("Screen", back_populates="instances")
    children = relationship(
        "ComponentInstance",
        backref=backref("parent", remote_side=[id]),
        cascade="all, delete-orphan"
    )
