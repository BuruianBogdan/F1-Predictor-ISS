from repositories.driver_repository import DriverRepository


class DriverService:

    def __init__(self):
        self.repo = DriverRepository()

    def get_drivers(self):
        drivers = self.repo.get_all_drivers()
        return [driver.to_dict() for driver in drivers]

    def create_driver(self, driver_data):
        driver = self.repo.add_driver(driver_data)
        return driver.to_dict()

    def remove_driver(self, driver_id):
        self.repo.delete_driver(driver_id)