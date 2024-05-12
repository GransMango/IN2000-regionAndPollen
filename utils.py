from shapely.geometry import Point
from config import GDF

def find_region(lat, lon):
    point = Point(lon, lat)
    for idx, row in GDF.iterrows():
        if row.geometry.contains(point):
            return row['fylkesnavn']
    return "Error, region not found"
