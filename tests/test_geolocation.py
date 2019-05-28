import pytest
import dramatiq
import geolocation
import geocoder
from dramatiq import Message, Middleware


def test_actor_geo_location(stub_broker):
    @dramatiq.actor
    def geo_location(location):
        return geocoder.osm(location)
    # assert isinstance(geo_location("Buddingevej 152800 Kongens Lyngby"), dramatiq.Actor)
    assert geo_location.actor_name == "geo_location"


def test_actor_geo_location_address(stub_broker):
    @dramatiq.actor
    def geo_location(location):
        return geocoder.osm(location).latlng
    assert geo_location("Buddingevej 152800 Kongens Lyngby") == [55.7673935, 12.4980629]


def test_actor_geo_location_coordinates(stub_broker):
    @dramatiq.actor
    def geo_location(location):
        return geocoder.osm(location, method="reverse").street
    assert geo_location("55.674146, 12.569553") == "Tietgensgade"


def test_actor_geo_location_message(stub_broker):
    @dramatiq.actor
    def geo_location(location):
        return geocoder.osm(location, method="reverse").street
    
    _message = geo_location.send("55.674146, 12.569553")
    _message_data = stub_broker.queues["default"].get(timeout=1)
    assert _message == Message.decode(_message_data)


def test_geo_location_success_callbacks(stub_broker, stub_worker):
    @dramatiq.actor
    def geo_location(location):
        return geocoder.osm(location).latlng

    message = []

    @dramatiq.actor
    def store_result(message_data, result):
        message.append(result)
    
    address = "H. C. Andersens Blvd. 27, 1553 København V, Denmark"
    geo_location.send_with_options(args=(address,), on_success=store_result)
    stub_broker.join(geo_location.queue_name)
    stub_worker.join()
    assert message == [[55.674136, 12.571782]]

