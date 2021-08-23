from pycoordinates.test.test_pycoordinates import TestSuite
from setuptools import setup, find_packages
# import 

setup(  name='pycoordinates',
        version= '0.1',
        description='A Python package that gives the location of the given coordinates, or\
                    gives the coordinates to a given location.',
        long_description=open('README.rst').read(),
        url='https://github.com/leeway64/pycoordinates',
        author='leeway64',
        packages=find_packages(),
        zip_safe=False,
        install_requires='geopy')
