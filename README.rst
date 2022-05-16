pycoordinates
=============

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: LICENSE.txt


pycoordinates is a command-line interface (CLI) Python package that tells you the location of the
given coordinates or gives the coordinates to a given location.


Installation
------------

.. code-block::

    pip install git+https://github.com/leeway64/pycoordinates.git#egg=pycoordinates


Basic usage
------------

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


Refer to the `usage examples <docs/usage_examples.rst>`_ for more information on how to run
these commands.


Tests
------

Travis CI will run unit tests automatically with each commit, but if you wish, you may run unit
tests manually.

To run unit tests, run, in the top-level directory:

.. code-block::

    pip install -r test_requirements.txt
    pytest --pyargs pycoordinates


Third Party Software
---------------------

- `geopy <https://pypi.org/project/geopy/>`_ (MIT License): Python client for online geocoding services.
- `pytest <https://docs.pytest.org/en/6.2.x/index.html>`_ (MIT License): Python testing framework.
