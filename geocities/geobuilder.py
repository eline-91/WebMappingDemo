from shapely.geometry import Point


def point(lat, lon, srs="EPSG:4326"):
    """Create shapely Point geometry from lat and long strings

    Args:
        lat (str): lattitude
        lon (str): longitue

    Returns:
        shapely Point object
    """
    return Point(float(lat), float(lon))
