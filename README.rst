pycoordinates
=============

pycoordinates is a Python package that tells you the location of the given coordinates, or gives
the coordinates to a given location.



Installation
------------

Using pip:

``pip install https://github.com/leeway64/pycoordinates.git#egg=pycoordinates``




Basic usage
------------

pycoordinates is a command-line interface (CLI); you will be able to run these commands in the
terminal of the directory where you installed this package.

::

  usage: pycoordinates [-h] [--coordinates COORDINATES COORDINATES]
                      [--location LOCATION] [--verbose]

  Provides information on given coordinates and returns coordinates of given
  location.

  optional arguments:
    -h, --help            show this help message and exit
    --coordinates COORDINATES COORDINATES
                          Latitude and longitude
    --location LOCATION   Name of the location
    --verbose             Produces a more verbose output


Refer to the `usage examples <docs/usage_examples.rst>`_ for more information on how to run
these commands.

References
-----------

`geopy <https://pypi.org/project/geopy/>`_ was an incredibly valuable Python package for this
project; it served as the backbone for the geolocation aspects of it.
