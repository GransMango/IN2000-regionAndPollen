from flask import Blueprint, request, jsonify
from shapely.geometry import Point
from config import GDF

region_bp = Blueprint('region', __name__)


def find_region(lat, lon, gdf):
    point = Point(lon, lat)
    for idx, row in gdf.iterrows():
        if row.geometry.contains(point):
            return row['fylkesnavn']
    return "Error, region not found"


@region_bp.route('/find_region', methods=['GET'])
def find_region_endpoint():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Please provide both 'lat' and 'lon' parameters"}), 400

    region = find_region(lat, lon, GDF)
    return jsonify({"region": region})
