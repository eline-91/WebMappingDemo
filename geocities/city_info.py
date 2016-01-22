from input_output import read_txt, write_shape
from apis import get_latlong
from apis import get_height_ahn2
from geobuilder import point

from shapely.geometry import mapping


# files
in_cities = 'cities.txt'
out_shape = '/home/user/Projects/webmappingdemo/shapefiles/city_info_result.shp'

# we want the data to look like this
schema = {'geometry': 'Point',
          'properties': {'city':'str',
                         'height_ahn2': 'float'}}


# we want to store the results in a list
results = []

# read text file with cities
cities = read_txt(in_cities)

# main loop
for city in cities:
    city = city.strip()
    print city

    location = get_latlong(city)
    print location

    geometry = point(location['lng'],location['lat'])
    geometry_wkt = geometry.wkt
    height_ahn2 = get_height_ahn2(geometry_wkt)

    results.append({'geometry': mapping(geometry),
                    'properties': {'city': city,
                                   'height_ahn2': height_ahn2}})

# save the results to a shapefile
write_shape(out_shape, schema, results)
