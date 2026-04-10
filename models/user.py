from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime 
from sqlalchemy.orm import relationship
from config.base import Base  

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    created_at = Column(DateTime, default=func.now())
    company = relationship("Company", back_populates="users")

    def __repr__(self):
        return f"<User {self.name}>"
