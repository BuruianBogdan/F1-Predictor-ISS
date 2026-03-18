from repositories.circuit_repository import CircuitRepository


class CircuitService:

    def __init__(self):
        self.repo = CircuitRepository()

    def get_circuits(self):
        circuits = self.repo.get_all_circuits()
        return [circuit.to_dict() for circuit in circuits]

    def get_circuit(self, circuit_id):
        circuit = self.repo.get_circuit(circuit_id)
        if circuit:
            return circuit.to_dict()
        return None

    def create_circuit(self, circuit_data):
        circuit = self.repo.add_circuit(circuit_data)
        return circuit.to_dict()

    def update_circuit(self, circuit_id, circuit_data):
        circuit = self.repo.update_circuit(circuit_id, circuit_data)
        if circuit:
            return circuit.to_dict()
        return None

    def remove_circuit(self, circuit_id):
        self.repo.delete_circuit(circuit_id)