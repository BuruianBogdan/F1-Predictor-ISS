from flask import Flask
from api.driver_routes import driver_bp
from api.constructor_routes import constructor_bp
from api.circuit_routes import circuit_bp
from api.race_routes import race_bp
from api.result_routes import result_bp
from api.import_routes import import_bp
from api.standings_routes import standings_bp
from api.prediction_routes import prediction_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(driver_bp)
    app.register_blueprint(constructor_bp)
    app.register_blueprint(circuit_bp)
    app.register_blueprint(race_bp)
    app.register_blueprint(result_bp)
    app.register_blueprint(import_bp)
    app.register_blueprint(standings_bp)
    app.register_blueprint(prediction_bp)

    print(app.url_map)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)