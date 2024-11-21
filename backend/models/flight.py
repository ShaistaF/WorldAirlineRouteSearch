from .database import db

def get_optimized_route(origin, destination):

    return {
        'origin': origin,
        'destination': destination,
        'route': [origin, 'Waypoint1', 'Waypoint2', destination],
        'distance': '500 nautical miles'
    }
