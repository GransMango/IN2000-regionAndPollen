import os
import geopandas as gpd
import requests

def download_geojson():
    url = os.getenv('REGION_DATA_URL')  # The SAS URL for the file
    response = requests.get(url)
    os.makedirs('data', exist_ok=True)
    with open('data/Basisdata_0000_Norge_25833_Fylker_GeoJSON.geojson', 'wb') as f:
        f.write(response.content)

def load_geojson():
    data_path = 'data/Basisdata_0000_Norge_25833_Fylker_GeoJSON.geojson'
    
    if not os.path.exists(data_path):
        download_geojson()
    
    gdf = gpd.read_file(data_path)

    if gdf.crs is None:
        gdf = gdf.to_crs("EPSG:4326")
    else:
        gdf = gdf.to_crs("EPSG:4326")

    if 'fylkesnavn' not in gdf.columns:
        gdf['fylkesnavn'] = gdf['properties'].apply(lambda x: x['fylkesnavn'] if 'fylkesnavn' in x else 'Unknown')

    return gdf

GDF = load_geojson()
