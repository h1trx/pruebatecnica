from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.orm import relationship
from config.db import Base

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    company_id = Column(Integer, ForeignKey("companies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())
    company = relationship("Company", back_populates="products")
    user = relationship("User")

    def __repr__(self):
        pass
