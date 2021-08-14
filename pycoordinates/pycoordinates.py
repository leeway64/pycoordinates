import argparse


def parse_commands():
    parser = argparse.ArgumentParser(description="Provides information on give coordinates")
    parser.add_argument('--coordinates', action='store', nargs=2, help='Latitude and longitude')
    parser.add_argument('--location', action='store', nargs=1, help='Name of the location')
    parser.add_argument('--cardinal', action='store_true', nargs=1, help='Allows for cardinal\
    coordinates to be typed (e.g., 25N, 121E)')

if __name__ == '__main__':
    parse_commands()
