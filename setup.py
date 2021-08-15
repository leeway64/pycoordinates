from setuptools import setup, find_packages

setup(  name='pycoordinates',
        version='1.0',
        description='A Python package that tells you the location of the given coordinates, or\
                    gives the coordinates to a given location.',
        long_description=open('README.rst').read(),
        url='https://github.com/leeway64/pycoordinates',
        author='leeway64',
        packages=find_packages(),
        zip_safe=False,
        install_requires='geopy')
