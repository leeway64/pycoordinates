import setuptools
from pycoordinates.__init__ import __version__

with open('README.rst', 'r') as README:
    long_description = README.read()

setuptools.setup(   name='pycoordinates',
                    version= __version__,
                    description='A Python package that gives the location of the given coordinates, or\
                                gives the coordinates to a given location.',
                    long_description=long_description,
                    url='https://github.com/leeway64/pycoordinates',
                    author='leeway64',
                    packages=setuptools.find_packages(),
                    entry_points={'console_scripts':['pycoordinates=pycoordinates.pycoordinates:\
                                    parse_commands']},
                    install_requires='geopy',
                    python_requires='>=3.8')
