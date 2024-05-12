import geopandas as gpd

def load_geojson():
    geojson_file = 'data/Basisdata_0000_Norge_25833_Fylker_GeoJSON.geojson'
    gdf = gpd.read_file(geojson_file)

    if gdf.crs is None:
        gdf = gdf.to_crs("EPSG:4326")
    else:
        gdf = gdf.to_crs("EPSG:4326")

    if 'fylkesnavn' not in gdf.columns:
        gdf['fylkesnavn'] = gdf['properties'].apply(lambda x: x['fylkesnavn'] if 'fylkesnavn' in x else 'Unknown')

    return gdf

GDF = load_geojson()
