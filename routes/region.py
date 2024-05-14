from flask import Blueprint, request, jsonify
from utils import find_kommune, map_kommune_to_pollenregion

region_bp = Blueprint('region', __name__)

@region_bp.route('/find_region', methods=['GET'])
def find_region_endpoint():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Please provide both 'lat' and 'lon' parameters"}), 400

    kommune = find_kommune(lat, lon)
    if kommune.startswith("Error"):
        return jsonify({"error": kommune}), 404

    pollen_region = map_kommune_to_pollenregion(kommune)
    if pollen_region.startswith("Error"):
        return jsonify({"error": pollen_region}), 404

    return jsonify({"kommune": kommune, "pollen_region": pollen_region})
