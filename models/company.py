from sqlalchemy import Column, func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime 
from sqlalchemy.orm import relationship
from config.base import Base

from sqlalchemy.dialects.postgresql import UUID
import uuid

class Company(Base):
    __tablename__ = "companies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(150), unique=True)
    created_at = Column(DateTime, default=func.now())
    products = relationship("Product", back_populates="company")
    users = relationship("User", back_populates="company")

    def __repr__(self):
        return f"<Company {self.name}>"