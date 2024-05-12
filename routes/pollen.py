import requests
from flask import Blueprint, request, jsonify
from utils import find_region
from config import API_KEY, BASE_URL

pollen_bp = Blueprint('pollen', __name__)

@pollen_bp.route('/pollen', methods=['GET'])
def get_pollen_data():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Please provide both 'lat' and 'lon' parameters"}), 400

    region = find_region(lat, lon)
    if region == "Error, region not found":
        return jsonify({"error": region}), 404

    region_id = get_region_id(region)
    if region_id is None:
        return jsonify({"error": "Region ID not found"}), 404

    response = requests.get(f"{BASE_URL}/region/{region_id}", headers={
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    })

    if response.status_code == 200:
        return jsonify({"region": region, "pollen_data": response.json()})
    elif response.status_code == 401:
        return jsonify({"error": "Unauthorized access. Check API key setup in readme."}), 401
    elif response.status_code == 403:
        return jsonify({"error": "Forbidden access. You don't have access to the resource."}), 403
    elif response.status_code == 404:
        return jsonify({"error": "Resource not found. Check the URL."}), 404
    elif response.status_code == 400:
        return jsonify({"error": "Bad request. Check the URL, specifically if regionId is legal."}), 400
    else:
        return jsonify({"error": f"Error fetching pollen data for region {region_id}: {response.status_code}"}), 500

def get_region_id(region_name):
    response = requests.get(f"{BASE_URL}/regions", headers={
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    })

    if response.status_code == 200:
        regions = response.json()
        for region in regions:
            if region["displayName"] == region_name:
                return region["id"]
    return None

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
