Usage examples
===============

Display help
---------------

.. code-block::

    $ pycoordinates --help

    usage: pycoordinates [-h] [--coordinates COORDINATES COORDINATES] [--location LOCATION] [--verbose]

    Provides information on given coordinates and returns coordinates of given location.

    options:
      -h, --help            show this help message and exit
      --coordinates COORDINATES COORDINATES
                            Latitude and longitude
      --location LOCATION   Name of the location
      --verbose             Produces a more verbose output


Find location
---------------

**Example 1:**

.. code-block::

    $ pycoordinates --coordinates 32.72 117.16W

    San Diego, California, United States


**Example 2:**

.. code-block::

    $ pycoordinates --coordinates 37.57 126.98

    Seoul, South Korea


Find coordinates
------------------

.. code-block::

    $ pycoordinates --location "Taipei, Taiwan"

    Taipei, Taiwan: 25.04, 121.56


Find location (verbose)
---------------------------

.. code-block::

    $ pycoordinates --verbose --coordinates 37.57 126.98

    City: Seoul
    Country: South Korea


Find coordinates (verbose)
-----------------------------

.. code-block::

    $ pycoordinates --verbose --location "Taipei, Taiwan"

    Location: Taipei, Taiwan
    Latitude: 25.04
    Longitude: 121.56
