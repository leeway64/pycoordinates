from pycoordinates.test.test_pycoordinates import TestSuite
from setuptools import setup, find_packages
from pycoordinates.__init__ import __version__

with open('README.rst', 'r') as README:
    long_description = README.read()

setup(  name='pycoordinates',
        version= __version__,
        description='A Python package that gives the location of the given coordinates, or\
                    gives the coordinates to a given location.',
        long_description=long_description,
        url='https://github.com/leeway64/pycoordinates',
        author='leeway64',
        packages=find_packages(),
        install_requires='geopy')
