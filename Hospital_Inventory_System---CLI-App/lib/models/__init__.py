from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///hospital_inventory.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()


def init_db():
    from .patient import Patient
    from .doctor import Doctor
    from .appointment import Appointment
    from .user import User
    from .role import Role

    Base.metadata.create_all(engine)
