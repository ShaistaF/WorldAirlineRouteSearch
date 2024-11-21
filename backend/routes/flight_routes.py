from flask import Blueprint, request, jsonify
from models.flight import get_optimized_route

flight_bp = Blueprint('flight', __name__)

@flight_bp.route('/optimize', methods=['POST'])
def optimize_flight():
    data = request.json
    origin = data.get('origin')
    destination = data.get('destination')
    if not origin or not destination:
        return jsonify({'error': 'Origin and destination are required'}), 400

    route = get_optimized_route(origin, destination)
    return jsonify(route)
