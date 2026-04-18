from datetime import datetime
from database.db import SessionLocal
from models.race_result import RaceResult


class ResultRepository:

    def get_all_results(self):
        session = SessionLocal()
        results = session.query(RaceResult).all()
        session.close()
        return results

    def get_result(self, result_id):
        session = SessionLocal()
        result = session.query(RaceResult).filter(RaceResult.result_id == result_id).first()
        session.close()
        return result

    def get_results_by_race(self, race_id):
        session = SessionLocal()
        results = session.query(RaceResult).filter(RaceResult.race_id == race_id).all()
        session.close()
        return results

    def add_result(self, result_data):
        session = SessionLocal()

        result = RaceResult(
            race_id=result_data["race_id"],
            driver_id=result_data["driver_id"],
            constructor_id=result_data["constructor_id"],
            grid=result_data.get("grid"),
            position=result_data.get("position"),
            points=result_data.get("points", 0.0),
            status=result_data.get("status", "Finished")
        )

        session.add(result)
        session.commit()
        session.refresh(result)
        session.close()

        return result

    def update_result(self, result_id, result_data):
        session = SessionLocal()

        result = session.query(RaceResult).filter(RaceResult.result_id == result_id).first()
        if not result:
            session.close()
            return None

        if "race_id" in result_data:
            result.race_id = result_data["race_id"]
        if "driver_id" in result_data:
            result.driver_id = result_data["driver_id"]
        if "constructor_id" in result_data:
            result.constructor_id = result_data["constructor_id"]
        if "grid" in result_data:
            result.grid = result_data["grid"]
        if "position" in result_data:
            result.position = result_data["position"]
        if "points" in result_data:
            result.points = result_data["points"]
        if "status" in result_data:
            result.status = result_data["status"]

        session.commit()
        session.refresh(result)
        session.close()

        return result

    def delete_result(self, result_id):
        session = SessionLocal()

        result = session.query(RaceResult).filter(RaceResult.result_id == result_id).first()
        if not result:
            session.close()
            return False

        session.delete(result)
        session.commit()
        session.close()

        return True