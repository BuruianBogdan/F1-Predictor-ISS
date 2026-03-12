from database.db import SessionLocal
from models.constructor import Constructor


class ConstructorRepository:

    def get_all_constructors(self):
        session = SessionLocal()
        constructors = session.query(Constructor).all()
        session.close()
        return constructors

    def get_constructor(self, constructor_id):
        session = SessionLocal()
        constructor = session.query(Constructor).filter(Constructor.constructor_id == constructor_id).first()
        session.close()
        return constructor

    def add_constructor(self, constructor_data):
        session = SessionLocal()

        constructor = Constructor(
            constructor_ref=constructor_data["constructor_ref"],
            name=constructor_data["name"],
            nationality=constructor_data["nationality"]
        )

        session.add(constructor)
        session.commit()
        session.refresh(constructor)
        session.close()

        return constructor

    def update_constructor(self, constructor_id, constructor_data):
        session = SessionLocal()

        constructor = session.query(Constructor).filter(
            Constructor.constructor_id == constructor_id
        ).first()

        if not constructor:
            session.close()
            return None

        if "constructor_ref" in constructor_data:
            constructor.constructor_ref = constructor_data["constructor_ref"]
        if "name" in constructor_data:
            constructor.name = constructor_data["name"]
        if "nationality" in constructor_data:
            constructor.nationality = constructor_data["nationality"]

        session.commit()
        session.refresh(constructor)
        session.close()

        return constructor

    def delete_constructor(self, constructor_id):
        session = SessionLocal()

        constructor = session.query(Constructor).filter(
            Constructor.constructor_id == constructor_id
        ).first()

        if constructor:
            session.delete(constructor)
            session.commit()

        session.close()