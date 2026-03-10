from sqlalchemy import Column, Integer, String, Float
from database.db import Base


class RaceResult(Base):
    __tablename__ = "race_results"

    result_id = Column(Integer, primary_key=True, autoincrement=True)
    race_id = Column(Integer)
    driver_id = Column(Integer)
    constructor_id = Column(Integer)
    grid = Column(Integer)
    position = Column(Integer)
    points = Column(Float)
    status = Column(String)