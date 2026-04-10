from sqlalchemy import Table, Column, func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime 
from config.db import Base

class Users(Base):
    __tablename_ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    company_id = Column(Integer, nullable=False)
    create_at = Column(DateTime, default=func.now())

    def __repr__(self):
        pass
