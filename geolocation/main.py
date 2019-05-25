import dramatiq
import requests
import sys
import geocoder
from utils import logger

from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dramatiq.results import Results
from dramatiq.results.backends import StubBackend
result_backend = StubBackend()
broker = RabbitmqBroker()
broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(broker)


@dramatiq.actor
def print_result(message_data, result):
    logger.info(f"The result of message {message_data['message_id']} was {result}.")

@dramatiq.actor
def print_error(message_data, exception_data):
    logger.error(f"Message {message_data['message_id']} failed:")
    logger.error(f"  * type: {exception_data['type']}")
    logger.error(f"  * message: {exception_data['message']!r}")

@dramatiq.actor(store_results=True)
def geo_location(location):
    g = geocoder.osm(location)
    return g.json

def main(args):
    message = geo_location.send_with_options(
        args=(args,) ,
        on_failure=print_error, 
        on_success=print_result,)

    result = message.get_result(block=True)
    logger.debug("Message result {result}")

if __name__ == "__main__":
    main(sys.argv[1])