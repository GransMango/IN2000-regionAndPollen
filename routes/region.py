from flask import Blueprint, request, jsonify
from utils import find_region

region_bp = Blueprint('region', __name__)

@region_bp.route('/find_region', methods=['GET'])
def find_region_endpoint():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Please provide both 'lat' and 'lon' parameters"}), 400

    region = find_region(lat, lon)
    return jsonify({"region": region})
