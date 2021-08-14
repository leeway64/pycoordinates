import argparse


def parse_commands():
    parser = argparse.ArgumentParser(prog='pycoordinates', description="Provides information \
                                on given coordinates and returns coordinates of given location")
    parser.version = 1.0

    parser.add_argument('--coordinates', action='store', nargs=2, help='Latitude and longitude')
    parser.add_argument('--location', action='store', nargs=1, help='Name of the location')
    parser.add_argument('--cardinal', action='store_true', help='Allows for cardinal coordinates\
                                                                to be typed (e.g., 25N, 121E)')
    parser.add_argument('--version', action='version')

if __name__ == '__main__':
    parse_commands()
