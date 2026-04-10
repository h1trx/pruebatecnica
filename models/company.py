from sqlalchemy import Column, func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime 
from sqlalchemy.orm import relationship
from config.base import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True)
    created_at = Column(DateTime, default=func.now())
    products = relationship("Products", back_populates="company")
    users = relationship("User", back_populates="company")

    def __repr__(self):
        pass