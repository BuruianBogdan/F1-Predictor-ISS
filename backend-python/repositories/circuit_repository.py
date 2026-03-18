from database.db import SessionLocal
from models.circuit import Circuit


class CircuitRepository:

    def get_all_circuits(self):
        session = SessionLocal()
        circuits = session.query(Circuit).all()
        session.close()
        return circuits

    def get_circuit(self, circuit_id):
        session = SessionLocal()
        circuit = session.query(Circuit).filter(Circuit.circuit_id == circuit_id).first()
        session.close()
        return circuit

    def add_circuit(self, circuit_data):
        session = SessionLocal()

        circuit = Circuit(
            circuit_ref=circuit_data["circuit_ref"],
            name=circuit_data["name"],
            location=circuit_data["location"],
            country=circuit_data["country"],
            lat=circuit_data["lat"],
            lng=circuit_data["lng"]
        )

        session.add(circuit)
        session.commit()
        session.refresh(circuit)
        session.close()

        return circuit

    def update_circuit(self, circuit_id, circuit_data):
        session = SessionLocal()

        circuit = session.query(Circuit).filter(Circuit.circuit_id == circuit_id).first()

        if not circuit:
            session.close()
            return None

        if "circuit_ref" in circuit_data:
            circuit.circuit_ref = circuit_data["circuit_ref"]
        if "name" in circuit_data:
            circuit.name = circuit_data["name"]
        if "location" in circuit_data:
            circuit.location = circuit_data["location"]
        if "country" in circuit_data:
            circuit.country = circuit_data["country"]
        if "lat" in circuit_data:
            circuit.lat = circuit_data["lat"]
        if "lng" in circuit_data:
            circuit.lng = circuit_data["lng"]

        session.commit()
        session.refresh(circuit)
        session.close()

        return circuit

    def delete_circuit(self, circuit_id):
        session = SessionLocal()

        circuit = session.query(Circuit).filter(Circuit.circuit_id == circuit_id).first()

        if circuit:
            session.delete(circuit)
            session.commit()

        session.close()