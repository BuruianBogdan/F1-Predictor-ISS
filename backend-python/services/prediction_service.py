from repositories.driver_repository import DriverRepository
from repositories.result_repository import ResultRepository
from repositories.constructor_repository import ConstructorRepository


class PredictionService:
    def __init__(self):
        self.driver_repo = DriverRepository()
        self.result_repo = ResultRepository()
        self.constructor_repo = ConstructorRepository()

    # CU-10: Predict Championship
    def predict_champion(self):
        drivers = self.driver_repo.get_all_drivers()
        results = self.result_repo.get_all_results()

        driver_stats = {}

        for driver in drivers:
            driver_stats[driver.driver_id] = {
                "driver": driver,
                "points": 0,
                "finishes": [],
                "dnf": 0
            }

        for result in results:
            stats = driver_stats.get(result.driver_id)
            if not stats:
                continue

            stats["points"] += result.points

            if result.status == "Finished" and result.position is not None:
                stats["finishes"].append(result.position)
            else:
                stats["dnf"] += 1

        predictions = []

        for _, stats in driver_stats.items():
            avg_finish = (
                sum(stats["finishes"]) / len(stats["finishes"])
                if stats["finishes"] else 20
            )

            score = (
                    stats["points"] * 0.6 +
                    (20 - avg_finish) * 10 * 0.3 -
                    stats["dnf"] * 5 * 0.1
            )

            driver = stats["driver"]
            full_name = f"{driver.forename} {driver.surname}"

            predictions.append({
                "driver_id": driver.driver_id,
                "name": full_name,
                "code": driver.code,
                "predicted_score": round(score, 2)
            })

        predictions.sort(key=lambda x: x["predicted_score"], reverse=True)

        return predictions

    # CU-11: Predict Race
    def predict_race(self, race_id):
        results = self.result_repo.get_results_by_race(race_id)

        predictions = []

        for r in results:
            finish_position = r.position if r.position is not None else 20

            score = (
                    (20 - finish_position) * 0.5 +
                    r.points * 0.3 +
                    (5 if r.status == "Finished" else 0)
            )

            predictions.append({
                "result_id": r.result_id,
                "driver_id": r.driver_id,
                "constructor_id": r.constructor_id,
                "grid": r.grid,
                "position": r.position,
                "points": r.points,
                "status": r.status,
                "predicted_score": round(score, 2)
            })

        predictions.sort(key=lambda x: x["predicted_score"], reverse=True)

        return predictions