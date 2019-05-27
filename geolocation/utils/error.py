
class GeolocationError(Exception):
    """
    Base class for Geolocation errors
    """

    def __init__(self, message='', details=''):
        Exception.__init__(self, message)
        self.details = details

    @property
    def message(self):
        print(self)
    

    class DataError(GeolocationError):
        """
        Data error
        """