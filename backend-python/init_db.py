from database.db import engine, Base

import models.driver
import models.constructor
import models.circuit
import models.race
import models.race_result

print("Initializing database...")

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")