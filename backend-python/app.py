from flask import Flask, jsonify, request
from api.driver_routes import driver_bp
from api.constructor_routes import constructor_bp
from api.circuit_routes import circuit_bp
from api.race_routes import race_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(driver_bp)
    app.register_blueprint(constructor_bp)
    app.register_blueprint(circuit_bp)
    app.register_blueprint(race_bp)
    return app
app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
