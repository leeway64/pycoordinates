from pycoordinates.pycoordinates import get_location, get_coordinates


class TestSuite:
    def test_get_location(self):
        verbose = False
        
        coordinates = (47.60, -122.33)
        assert get_location(*coordinates, verbose) == "Seattle, Washington, United States"

        coordinates = (40.73, -73.94)
        assert get_location(*coordinates, verbose) == "New York, New York, United States"

        coordinates = (48.86, 2.35)
        assert get_location(*coordinates, verbose) == "Paris, France"

        coordinates = (1.29, 103.85)
        assert get_location(*coordinates, verbose) == "Singapore, Singapore"

        coordinates = ['jdsfjdsfjsl', 7878347878]
        assert get_location(*coordinates, verbose) == "Invalid coordinates entered"        

    def test_get_coordinates(self):
        verbose = False
        
        location = "Seattle, Washington"
        assert get_coordinates(location, verbose) == f"{location}: 47.60, -122.33"

        location = "Taipei Taiwan"
        assert get_coordinates(location, verbose) == f"{location}: 25.04, 121.56"

        location = "seoul south korea"
        assert get_coordinates(location, verbose) == f"{location}: 37.57, 126.98"

        location = "england london"
        assert get_coordinates(location, verbose) == f"{location}: 51.51, -0.13"

        location = "sfsdfdsfdsfsdfdsf"
        assert get_coordinates(location, verbose) == "Invalid location entered"
