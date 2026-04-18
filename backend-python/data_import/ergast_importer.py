import requests


class ErgastImporter:
    """
    Folosim endpoint-uri Jolpica compatibile cu Ergast.
    """

    BASE_URL = "https://api.jolpi.ca/ergpyast/f1"

    def _get_json(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()

    def fetch_drivers(self, season):
        data = self._get_json(f"{season}/drivers.json?limit=1000")
        return data["MRData"]["DriverTable"]["Drivers"]

    def fetch_constructors(self, season):
        data = self._get_json(f"{season}/constructors.json?limit=1000")
        return data["MRData"]["ConstructorTable"]["Constructors"]

    def fetch_circuits(self, season):
        data = self._get_json(f"{season}/circuits.json?limit=1000")
        return data["MRData"]["CircuitTable"]["Circuits"]

    def fetch_races(self, season):
        data = self._get_json(f"{season}/races.json?limit=1000")
        return data["MRData"]["RaceTable"]["Races"]

    def fetch_results(self, season):
        data = self._get_json(f"{season}/results.json?limit=2000")
        return data["MRData"]["RaceTable"]["Races"]