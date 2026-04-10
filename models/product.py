from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.orm import relationship
from config.base import Base

from sqlalchemy.dialects.postgresql import UUID
import uuid

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255))
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())
    company = relationship("Company", back_populates="products")

    def __repr__(self):
        return f"<Product {self.name}>"
