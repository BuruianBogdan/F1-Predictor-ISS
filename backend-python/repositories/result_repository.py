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

    def add_result(self, result_data):
        session = SessionLocal()

        result = RaceResult(
            race_id=result_data["race_id"],
            driver_id=result_data["driver_id"],
            constructor_id=result_data["constructor_id"],
            grid=result_data["grid"],
            position=result_data["position"],
            points=result_data["points"],
            status=result_data["status"]
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

        if result:
            session.delete(result)
            session.commit()

        session.close()