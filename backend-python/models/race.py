from sqlalchemy import Column, Integer, String, Date
from database.db import Base


class Race(Base):
    __tablename__ = "races"

    race_id = Column(Integer, primary_key=True, autoincrement=True)
    season_year = Column(Integer)
    round = Column(Integer)
    circuit_id = Column(Integer)
    race_name = Column(String)
    date = Column(Date)
    is_completed = Column(Integer, default=0)