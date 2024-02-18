import json

from aiokafka import AIOKafkaProducer

from app.settings import settings


class AIOKafkaProducerConnection(AIOKafkaProducer):
    """AIOKafkaProducerConnection extends AIOKafkaProducer to provide a connection
    to a Kafka broker for asynchronous message production.

    Args:
    ----
        *args: Additional positional arguments to pass to AIOKafkaProducer.
        **kwargs: Additional keyword arguments to pass to AIOKafkaProducer.

    Note:
    ----
        This class sets default values for certain AIOKafkaProducer parameters
        to simplify the initialization process.

    Attributes:
    ----------
        bootstrap_servers (list): List of Kafka bootstrap servers.
        value_serializer (callable): Function to serialize message values.
    """

    def __init__(self, *args, **kwargs):
        AIOKafkaProducer.__init__(
            self,
            bootstrap_servers=settings.BOOTSTRAP_SERVERS.split(sep=","),
            value_serializer=lambda message: json.dumps(
                message,
            ).encode("utf-8"),
            *args,
            **kwargs,
        )
