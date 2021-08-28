Usage examples
===============

Display help
---------------

``pycoordinates --help``


Find location
---------------

**Example 1:**

Input:

``pycoordinates --coordinates 32.72 117.16W``

Output:

``San Diego, California, United States``


**Example 2:**

Input:

``pycoordinates --coordinates 37.57 126.98``

Output:

``Seoul, South Korea``


Find coordinates
------------------

Input:

``pycoordinates --location "taipei taiwan"``

Output:

``Taipei, Taiwan: 25.04, 121.56``



Find location (verbose)
---------------------------

Input:

``pycoordinates --verbose --coordinates 37.57 126.98``


Output:

``City: Seoul

Country: South Korea``


Find coordinates (verbose)
-----------------------------

Input:

``pycoordinates --verbose --location "Taipei, Taiwan"``

Output:

``Location: Taipei, Taiwan

Latitude: 25.04

Longitude: 121.56``