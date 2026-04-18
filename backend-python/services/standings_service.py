from repositories.standings_repository import StandingsRepository


class StandingsService:

    def __init__(self):
        self.repo = StandingsRepository()

    def get_driver_standings(self):
        rows = self.repo.get_driver_standings()

        standings = []
        position = 1

        for row in rows:
            standings.append({
                "position": position,
                "driver_id": row.driver_id,
                "driver_name": f"{row.forename} {row.surname}",
                "code": row.code,
                "points": float(row.total_points) if row.total_points is not None else 0.0
            })
            position += 1

        return standings

    def get_constructor_standings(self):
        rows = self.repo.get_constructor_standings()

        standings = []
        position = 1

        for row in rows:
            standings.append({
                "position": position,
                "constructor_id": row.constructor_id,
                "constructor_name": row.name,
                "nationality": row.nationality,
                "points": float(row.total_points) if row.total_points is not None else 0.0
            })
            position += 1

        return standings