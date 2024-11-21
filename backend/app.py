from flask import Flask
from routes.flight_routes import flight_bp
from routes.weather import weather_bp
from models.database import init_db
import config

app = Flask(__name__)
app.config.from_object(config.Config)

# Initialize database
init_db(app)

# Register Blueprints
app.register_blueprint(flight_bp, url_prefix='/api/flights')
app.register_blueprint(weather_bp, url_prefix='/api/weather')

if __name__ == "__main__":
    app.run(debug=True)
