from sqlalchemy import Column, String, Integer, JSON, Enum, UniqueConstraint
from sqlalchemy.orm import declarative_base
import enum

Base = declarative_base()

class ValueType(str, enum.Enum):
    number = "number"
    boolean = "boolean"
    string = "string"
    array = "array"
    json = "json"

class Parameter(Base):
    __tablename__ = "parameters"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True) 
    value = Column(JSON, nullable=True)
    value_type = Column(Enum(ValueType), nullable=False)
