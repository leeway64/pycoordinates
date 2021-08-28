import argparse
import time
from geopy.geocoders import Nominatim

app = Nominatim(user_agent="pycoordinates")


def get_location(latitude, longitude, verbose):
    '''Takes in a latitude and longitude and returns the commensurate location.
    :param latitude: the latitude
    :param longitude: the longitude
    :type latitude: float
    :type longitude: float
    :returns: the city that is found at the given coordinates
    :rtype: str
    :raises ValueError: raises a ValueError if latitude and/or longitude is not a coordinates
    '''
    coordinates = f"{latitude}, {longitude}"
    try:
        location_info = app.reverse(coordinates).raw
    except ValueError:
        return "Invalid coordinates entered"

    location = ''

    if verbose:
        location = location + f'City: {location_info["address"]["city"]}\n'
        
        if location_info["address"]['country'] == 'United States':
            location = location + f'State: {location_info["address"]["state"]}\n'
        
        location = location + f'Country: {location_info["address"]["country"]}\n'
    else:
        location = location + f'{location_info["address"]["city"]}, '
        
        if location_info["address"]['country'] == 'United States':
            location = location + f'{location_info["address"]["state"]}, '
        
        location = location + f'{location_info["address"]["country"]}'

    # Nominatim only allows 1 request per second
    time.sleep(1)

    return location


def get_coordinates(location, verbose):
    '''Takes in a location and returns its coordinates.
    :param location: the location that you want to find the coordinates of
    :type location: str
    :returns: the coordinates of the given location
    :rtype: str
    :raises AttributeError: raises an AttributeError if the given location is not a valid location
    '''
    try:
        location_info = app.geocode(location).raw
    except AttributeError:
        return "Invalid location entered"

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
    '''Command-line interface driver.'''
    parser = argparse.ArgumentParser(prog='pycoordinates', description="Provides information \
                                on given coordinates and returns coordinates of given location.")

    parser.add_argument('--coordinates', action='store', nargs=2, help='Latitude and longitude')
    parser.add_argument('--location', action='store', nargs=1, help='Name of the location')
    parser.add_argument('--verbose', action='store_true', help="Produces a more verbose output")


    arguments = parser.parse_args()

    if arguments.coordinates:
        latitude = arguments.coordinates[0]
        longitude = arguments.coordinates[1]
        print(get_location(latitude, longitude, arguments.verbose))

    if arguments.location:
        print(get_coordinates(arguments.location[0], arguments.verbose))

if __name__ == '__main__':
    parse_commands()
