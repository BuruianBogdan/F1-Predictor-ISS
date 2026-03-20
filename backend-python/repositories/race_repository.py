from datetime import datetime
from database.db import SessionLocal
from models.race import Race


class RaceRepository:

    def get_all_races(self):
        session = SessionLocal()
        races = session.query(Race).all()
        session.close()
        return races

    def get_race(self, race_id):
        session = SessionLocal()
        race = session.query(Race).filter(Race.race_id == race_id).first()
        session.close()
        return race

    def add_race(self, race_data):
        session = SessionLocal()

        race_date = None
        if race_data.get("date"):
            race_date = datetime.strptime(race_data["date"], "%Y-%m-%d").date()

        race = Race(
            season_year=race_data["season_year"],
            round=race_data["round"],
            circuit_id=race_data["circuit_id"],
            race_name=race_data["race_name"],
            date=race_date,
            is_completed=race_data.get("is_completed", 0)
        )

        session.add(race)
        session.commit()
        session.refresh(race)
        session.close()

        return race

    def update_race(self, race_id, race_data):
        session = SessionLocal()

        race = session.query(Race).filter(Race.race_id == race_id).first()

        if not race:
            session.close()
            return None

        if "season_year" in race_data:
            race.season_year = race_data["season_year"]
        if "round" in race_data:
            race.round = race_data["round"]
        if "circuit_id" in race_data:
            race.circuit_id = race_data["circuit_id"]
        if "race_name" in race_data:
            race.race_name = race_data["race_name"]
        if "date" in race_data and race_data["date"]:
            race.date = datetime.strptime(race_data["date"], "%Y-%m-%d").date()
        if "is_completed" in race_data:
            race.is_completed = race_data["is_completed"]

        session.commit()
        session.refresh(race)
        session.close()

        return race

    def delete_race(self, race_id):
        session = SessionLocal()

        race = session.query(Race).filter(Race.race_id == race_id).first()

        if race:
            session.delete(race)
            session.commit()

        session.close()