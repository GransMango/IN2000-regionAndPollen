from shapely.geometry import Point
from config import GDF, norway_kommuner, spatial_index

def find_kommune(lat, lon):
    # Create a point geometry
    point = Point(lon, lat)

    # Use the spatial index to find potential matches
    possible_matches_index = list(spatial_index.intersection(point.bounds))
    possible_matches = GDF.iloc[possible_matches_index]

    # Filter the possible matches to find the one that contains the point
    for idx, row in possible_matches.iterrows():
        if row.geometry.contains(point):
            # Extract the 'administrativenhetnavn' with "sprak" : "nor"
            admin_names = row.get('administrativenhetnavn', [])
            for name in admin_names:
                if isinstance(name, dict) and name.get('sprak') == 'nor':
                    return name.get('navn')
            # If no "nor" language name is found, return the 'kommunenavn'
            return row.get('kommunenavn', 'Unknown')
    return "Error, region not found"

def map_kommune_to_pollenregion(kommune):
    # Find the corresponding pollen region for the kommune
    pollen_region = norway_kommuner.get(kommune)
    if pollen_region is not None:
        return pollen_region
    return "Error, pollen region not found"
