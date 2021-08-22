from pycoordinates.pycoordinates import get_location, get_coordinates

class TestHarness:
    def test_get_location(self):
        assert get_location(47.606, -122.33, None) == "Seattle, Washington, United States"

    def test_get_coordinates(self):
        location = "Seattle, Washington"
        assert get_coordinates(location, None) == f"[\'{location}]\': 47.61, -122.33"
