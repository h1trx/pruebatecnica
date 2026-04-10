from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.orm import relationship
from config.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    company_id = Column(Integer, ForeignKey("companies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())
    company = relationship("Company", back_populates="products")

    def __repr__(self):
        return f"<Product {self.name}>"
