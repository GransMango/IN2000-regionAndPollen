import requests
from flask import Blueprint, request, jsonify
from utils import find_kommune, map_kommune_to_pollenregion
from config import API_KEY, BASE_URL

pollen_bp = Blueprint('pollen', __name__)

@pollen_bp.route('/pollen', methods=['GET'])
def get_pollen_data():
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

    response = requests.get(f"{BASE_URL}/region/{pollen_region}", headers={
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    })

    if response.status_code == 200:
        return jsonify({"kommune": kommune, "pollen_data": response.json()})
    elif response.status_code == 401:
        return jsonify({"error": "Unauthorized access. Check API key setup in readme."}), 401
    elif response.status_code == 403:
        return jsonify({"error": "Forbidden access. You don't have access to the resource."}), 403
    elif response.status_code == 404:
        return jsonify({"error": "Resource not found. Check the URL."}), 404
    elif response.status_code == 400:
        return jsonify({"error": "Bad request. Check the URL, specifically if regionId is legal."}), 400
    else:
        return jsonify({"error": f"Error fetching pollen data for region {pollen_region}: {response.status_code}"}), 500

@pollen_bp.route('/pollen/regions', methods=['GET'])
def get_pollen_regions():
    response = requests.get(f"{BASE_URL}/regions", headers={
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    })

    if response.status_code == 200:
        return jsonify(response.json())
    elif response.status_code == 401:
        return jsonify({"error": "Unauthorized access. Check API key setup in readme."}), 401
    elif response.status_code == 403:
        return jsonify({"error": "Forbidden access. You don't have access to the resource."}), 403
    elif response.status_code == 404:
        return jsonify({"error": "Resource not found. Check the URL."}), 404
    elif response.status_code == 400:
        return jsonify({"error": "Bad request. Check the URL."}), 400
    else:
        return jsonify({"error": f"Error fetching pollen regions: {response.status_code}"}), 500
