
from location import Location


class LocationSet:
    def __init__(self, num_of_locations: int):
        self._locations = [Location() for _ in range(num_of_locations)]

    @property
    def locations(self):
        return self._locations