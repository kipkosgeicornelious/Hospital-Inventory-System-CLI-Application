from sqlalchemy import Column, Integer, String
from . import Base


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
