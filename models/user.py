from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime 
from sqlalchemy.orm import relationship
from config.base import Base  

from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(60), unique=True)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"))
    created_at = Column(DateTime, default=func.now())
    company = relationship("Company", back_populates="users")

    def __repr__(self):
        return f"<User {self.name}>"
