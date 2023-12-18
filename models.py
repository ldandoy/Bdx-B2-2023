from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(255))
    ville = Column(String(255))
    mot_cle = Column(Text())
    type_event = Column(String(255))
