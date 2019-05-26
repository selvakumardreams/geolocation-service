import re
import dramatiq
import requests
import sys
import geocoder
from utils import logger
from location import Location

from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dramatiq.encoder import JSONEncoder
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend

result_backend = RedisBackend(encoder=JSONEncoder())
broker = RabbitmqBroker()
broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(broker)


def _validate_input(location):
    expr = r"[A-Za-z]+"
    pattern = re.compile(expr)
    match = pattern.findall(location)

    if len(match) == 0:
        # Provided input lat and long
        return True
    else:
        # Provided input address
        return False


@dramatiq.actor
def print_result(message_data, result):
    logger.info(
        f"The result of message {message_data['message_id']} was {result}.")


@dramatiq.actor
def print_error(message_data, exception_data):
    logger.error(f"Message {message_data['message_id']} failed:")
    logger.error(f"  * type: {exception_data['type']}")
    logger.error(f"  * message: {exception_data['message']!r}")


@dramatiq.actor(store_results=True)
def geo_location(location):
        if _validate_input(location):
            latlng = Location(location)
            location = latlng.lat, latlng.lang
            g = geocoder.osm(location, method="reverse")
            return g.street, g.housenumber, g.postal, g.city, g.country
        else:
            g = geocoder.osm(location)
            return g.latlng


def main(args):
    message = geo_location.send_with_options(
        args=(args,),
        on_failure=print_error,
        on_success=print_result,)

    result = result_backend.get_result(message, block=True)
    logger.info(str(result))

if __name__ == "__main__":
    main(sys.argv[1])
