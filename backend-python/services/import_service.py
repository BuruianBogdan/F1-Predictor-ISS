from datetime import datetime
from database.db import SessionLocal
from data_import.ergast_importer import ErgastImporter
from models.driver import Driver
from models.constructor import Constructor
from models.circuit import Circuit
from models.race import Race
from models.race_result import RaceResult


class ImportService:

    def __init__(self):
        self.importer = ErgastImporter()

    def import_historical_data(self, start_year, end_year):
        session = SessionLocal()

        imported_summary = {
            "drivers": 0,
            "constructors": 0,
            "circuits": 0,
            "races": 0,
            "results": 0
        }

        try:
            for season in range(start_year, end_year + 1):
                self._import_constructors(session, season, imported_summary)
                self._import_drivers(session, season, imported_summary)
                self._import_circuits(session, season, imported_summary)
                self._import_races(session, season, imported_summary)
                self._import_results(session, season, imported_summary)

            session.commit()
            return imported_summary

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def _import_drivers(self, session, season, summary):
        drivers = self.importer.fetch_drivers(season)

        for d in drivers:
            driver_ref = d.get("driverId")

            existing = session.query(Driver).filter(Driver.driver_ref == driver_ref).first()
            if existing:
                continue

            dob_value = None
            if d.get("dateOfBirth"):
                dob_value = datetime.strptime(d["dateOfBirth"], "%Y-%m-%d").date()

            driver = Driver(
                driver_ref=driver_ref,
                number=int(d["permanentNumber"]) if d.get("permanentNumber") else None,
                code=d.get("code"),
                forename=d.get("givenName"),
                surname=d.get("familyName"),
                dob=dob_value,
                nationality=d.get("nationality")
            )

            session.add(driver)
            summary["drivers"] += 1

        session.flush()

    def _import_constructors(self, session, season, summary):
        constructors = self.importer.fetch_constructors(season)

        for c in constructors:
            constructor_ref = c.get("constructorId")

            existing = session.query(Constructor).filter(
                Constructor.constructor_ref == constructor_ref
            ).first()

            if existing:
                continue

            constructor = Constructor(
                constructor_ref=constructor_ref,
                name=c.get("name"),
                nationality=c.get("nationality")
            )

            session.add(constructor)
            summary["constructors"] += 1

        session.flush()

    def _import_circuits(self, session, season, summary):
        circuits = self.importer.fetch_circuits(season)

        for c in circuits:
            circuit_ref = c.get("circuitId")

            existing = session.query(Circuit).filter(Circuit.circuit_ref == circuit_ref).first()
            if existing:
                continue

            location = c.get("Location", {})

            circuit = Circuit(
                circuit_ref=circuit_ref,
                name=c.get("circuitName"),
                location=location.get("locality"),
                country=location.get("country"),
                lat=float(location["lat"]) if location.get("lat") else None,
                lng=float(location["long"]) if location.get("long") else None
            )

            session.add(circuit)
            summary["circuits"] += 1

        session.flush()

    def _import_races(self, session, season, summary):
        races = self.importer.fetch_races(season)

        for r in races:
            round_number = int(r["round"]) if r.get("round") else None
            circuit_ref = r["Circuit"]["circuitId"]

            existing = session.query(Race).filter(
                Race.season_year == season,
                Race.round == round_number
            ).first()

            if existing:
                continue

            circuit = session.query(Circuit).filter(Circuit.circuit_ref == circuit_ref).first()
            if not circuit:
                continue

            race_date = None
            if r.get("date"):
                race_date = datetime.strptime(r["date"], "%Y-%m-%d").date()

            race = Race(
                season_year=season,
                round=round_number,
                circuit_id=circuit.circuit_id,
                race_name=r.get("raceName"),
                date=race_date,
                is_completed=1
            )

            session.add(race)
            summary["races"] += 1

        session.flush()

    def _import_results(self, session, season, summary):
        races_with_results = self.importer.fetch_results(season)

        for race_data in races_with_results:
            round_number = int(race_data["round"]) if race_data.get("round") else None

            race = session.query(Race).filter(
                Race.season_year == season,
                Race.round == round_number
            ).first()

            if not race:
                continue

            for result_data in race_data.get("Results", []):
                driver_ref = result_data["Driver"]["driverId"]
                constructor_ref = result_data["Constructor"]["constructorId"]

                driver = session.query(Driver).filter(Driver.driver_ref == driver_ref).first()
                constructor = session.query(Constructor).filter(
                    Constructor.constructor_ref == constructor_ref
                ).first()

                if not driver or not constructor:
                    continue

                existing = session.query(RaceResult).filter(
                    RaceResult.race_id == race.race_id,
                    RaceResult.driver_id == driver.driver_id
                ).first()

                if existing:
                    continue

                grid_position = None
                if result_data.get("grid") and str(result_data["grid"]).isdigit():
                    grid_position = int(result_data["grid"])

                finish_position = None
                if result_data.get("position") and str(result_data["position"]).isdigit():
                    finish_position = int(result_data["position"])

                points_value = float(result_data["points"]) if result_data.get("points") else 0.0
                status = result_data.get("status", "Unknown")

                race_result = RaceResult(
                    race_id=race.race_id,
                    driver_id=driver.driver_id,
                    constructor_id=constructor.constructor_id,
                    grid=grid_position,
                    position=finish_position,
                    points=points_value,
                    status=status
                )

                session.add(race_result)
                summary["results"] += 1

        session.flush()