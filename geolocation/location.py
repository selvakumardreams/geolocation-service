import re

class Location(object):
    """
    Location Object
    """
    lat = None
    lang = None

    def __init__(self, location):
        self.location = location
        self._validate_location(location)

    def _validate_location(self, location):
        if isinstance(location, str):
            expr = r"[-]?\d+[.]?[-]?[\d]+"
            pattern = re.compile(expr)
            match = pattern.findall(location)
            if len(match) == 2:
                lat, lang = match
                self._latlng_standard([lat, lang])

    def _latlng_standard(self, location):
        # https://gisgeography.com/latitude-longitude-coordinates/
        if len(location) == 2:
            lat = float(location[0])
            lang = float(location[1])

            if lat and lang:
                east_west = -90 <= lat <= 90
                north_south = -180 <= lang <= 180

                if east_west and north_south:
                    self.lat = lat
                    self.lang = lang
                    return self.lat, self.lang
                else:
                    raise ValueError("Not within geographical")
            else:
                raise ValueError("lat and lang should be numbers")


if __name__ == "__main__":
    latlng = Location("55.674136, 12.571782")
    location = latlng.lat, latlng.lang
    print(location)