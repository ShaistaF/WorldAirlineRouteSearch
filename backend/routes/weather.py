from flask import Blueprint, jsonify

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/conditions', methods=['GET'])
def get_weather_conditions():
    # Simulated weather response
    return jsonify({'weather': 'clear', 'wind_speed': '15 knots'})
