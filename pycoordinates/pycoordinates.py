import argparse
import time
from geopy.geocoders import Nominatim

app = Nominatim(user_agent="pycoordinates")


def get_location(latitude, longitude, verbose):
    coordinates = f"{latitude}, {longitude}"
    location_info = app.reverse(coordinates).raw

    location = ''

    if verbose:
        location = location + f'City: {location_info["address"]["city"]}\n'
        
        if location_info["address"]['country'] == 'United States':
            location = location + f'State: {location_info["address"]["state"]}\n'
        
        location = location + f'Country: {location_info["address"]["country"]}\n'
    else:
        location = location + f'{location_info["address"]["city"]}, '
        
        if location_info["address"]['country'] == 'United States':
            location = location + f'{location_info["address"]["state"]}'
        
        location = location + f'{location_info["address"]["country"]}'

    # Nominatim only allows 1 request per second
    time.sleep(1)

    return location


def get_coordinates(location, verbose):
    location_info = app.geocode(location).raw
    latitude = float(location_info["lat"])
    longitude = float(location_info["lon"])
    
    coordinates = ''

    if verbose:
        coordinates = coordinates + f'Location: {location}\n'
        coordinates = coordinates + f'Latitude: {latitude:.2f}\n'
        coordinates = coordinates + f'Longitude: {longitude:.2f}'
    else:
        coordinates = f'{location}: {latitude:.2f}, {longitude:.2f}'

    # Nominatim only allows 1 request per second
    time.sleep(1)

    return coordinates


def parse_commands():
    parser = argparse.ArgumentParser(prog='pycoordinates', description="Provides information \
                                on given coordinates and returns coordinates of given location")
    parser.version = 1.0

    parser.add_argument('--coordinates', action='store', nargs=2, help='Latitude and longitude')
    parser.add_argument('--location', action='store', nargs=1, help='Name of the location')
    parser.add_argument('--verbose', action='store_true', help="Produces a more verbose output")
    parser.add_argument('--version', action='version')


    arguments = parser.parse_args()

    if arguments.coordinates:
        latitude = arguments.coordinates[0]
        longitude = arguments.coordinates[1]
        print(get_location(latitude, longitude, arguments.verbose))

    if arguments.location:
        print(get_coordinates(arguments.location, arguments.verbose))

if __name__ == '__main__':
    parse_commands()
