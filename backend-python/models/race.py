from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database.db import Base


class Race(Base):
    __tablename__ = "races"

    race_id = Column(Integer, primary_key=True, autoincrement=True)
    season_year = Column(Integer, nullable=False)
    round = Column(Integer, nullable=False)
    circuit_id = Column(Integer, ForeignKey("circuits.circuit_id"))
    race_name = Column(String)
    date = Column(Date)
    is_completed = Column(Integer, default=0)

    def to_dict(self):
        return {
            "race_id": self.race_id,
            "season_year": self.season_year,
            "round": self.round,
            "circuit_id": self.circuit_id,
            "race_name": self.race_name,
            "date": str(self.date) if self.date else None,
            "is_completed": self.is_completed
        }