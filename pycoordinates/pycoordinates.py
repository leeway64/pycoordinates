import argparse
import time
from geopy.geocoders import Nominatim

app = Nominatim(user_agent="tutorial")


def get_location(latitude, longitude):
    coordinates = f"{latitude}, {longitude}"
    location_info = app.reverse(coordinates).raw
    
    print(f'Country: {location_info["country"]}')

    if location_info['country'] == 'United States':
        print(f'State: {location_info["state"]}')
    
    print(f'City: {location_info["city"]}')

    # Nominatim only allows 1 request per second
    time.sleep(1)


def get_coordinates(location):
    location_info = app.geocode(location).raw
    latitude = float(location_info["lat"])
    longitude = float(location_info["lon"])
    print(f'Location: {location}')
    print(f'Latitude: {latitude:.2f}')
    print(f'Longitude: {longitude:.2f}')

    # Nominatim only allows 1 request per second
    time.sleep(1)


def parse_commands():
    parser = argparse.ArgumentParser(prog='pycoordinates', description="Provides information \
                                on given coordinates and returns coordinates of given location")
    parser.version = 1.0

    parser.add_argument('--coordinates', action='store', nargs=2, help='Latitude and longitude')
    parser.add_argument('--location', action='store', nargs=1, help='Name of the location')
    parser.add_argument('--cardinal', action='store_true', help='Allows for cardinal coordinates\
                                                                to be typed (e.g., 25N, 121E)')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--version', action='version')


    arguments = parser.parse_args()

    if arguments.coordinates:
        latitude = arguments.coordinates[0]
        longitude = arguments.coordinates[1]
        get_location(latitude, longitude)
    elif arguments.coordinates and arguments.cardinal:
        pass

    if arguments.location:
        get_coordinates(arguments.location)
    elif arguments.location and arguments.cardinal:
        pass


if __name__ == '__main__':
    parse_commands()
