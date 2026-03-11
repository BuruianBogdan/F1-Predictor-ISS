from datetime import datetime
from database.db import SessionLocal
from models.driver import Driver


class DriverRepository:

    def get_all_drivers(self):
        session = SessionLocal()
        drivers = session.query(Driver).all()
        session.close()
        return drivers

    def get_driver(self, driver_id):
        session = SessionLocal()
        driver = session.query(Driver).filter(Driver.driver_id == driver_id).first()
        session.close()
        return driver

    def add_driver(self, driver_data):
        session = SessionLocal()

        data_nasterii = None
        if driver_data.get("dob"):
            data_nasterii = datetime.strptime(driver_data["dob"], "%Y-%m-%d").date()

        driver = Driver(
            driver_ref=driver_data["driver_ref"],
            number=driver_data["number"],
            code=driver_data["code"],
            forename=driver_data["forename"],
            surname=driver_data["surname"],
            dob=data_nasterii,
            nationality=driver_data["nationality"]
        )

        session.add(driver)
        session.commit()
        session.refresh(driver)
        session.close()

        return driver

    def delete_driver(self, driver_id):
        session = SessionLocal()
        driver = session.query(Driver).filter(Driver.driver_id == driver_id).first()

        if driver:
            session.delete(driver)
            session.commit()



    def update_driver(self, driver_data):
        session = SessionLocal()
        driver = session.query(Driver).filter(Driver.driver_id == driver_id).first()
        if not driver:
            session.close()
            return None

        if "driver_ref" in driver_data:
            driver.driver_ref = driver_data["driver_ref"]

        if "number" in driver_data:
            driver.number = driver_data["number"]

        if "code" in driver_data:
            driver.code = driver_data["code"]

        if "dob" in driver_data:
            driver.dob = driver_data["dob"]

        if "forname" in driver_data:
            driver.forename = driver_data["forname"]

        if "surname" in driver_data:
            driver.surname = driver_data["surname"]

        if "nationality" in driver_data:
            driver.nationality = driver_data["nationality"]

        if "dob" in driver_data:
            driver.dob = driver_data["dob"]

        session.add(driver)
        session.refresh(driver)
        session.close()
        return driver



