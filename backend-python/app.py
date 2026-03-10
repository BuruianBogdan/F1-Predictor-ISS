from flask import Flask, jsonify, request
from api.driver_routes import driver_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(driver_bp)
    return app
app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
