import json

from aiokafka import AIOKafkaConsumer

from app.settings import settings


class AIOKafkaConsumerConnection(AIOKafkaConsumer):
    """AIOKafkaConsumerConnection extends AIOKafkaConsumer to provide a connection
    to a Kafka broker for asynchronous consumption of messages.

    Args:
    ----
        *args: Additional positional arguments to pass to AIOKafkaConsumer.
        **kwargs: Additional keyword arguments to pass to AIOKafkaConsumer.

    Note:
    ----
        This class sets default values for certain AIOKafkaConsumer parameters
        to simplify the initialization process.

    Attributes:
    ----------
        bootstrap_servers (list): List of Kafka bootstrap servers.
        value_deserializer (callable): Function to deserialize message values.
    """

    def __init__(self, *args, **kwargs):
        AIOKafkaConsumer.__init__(
            self,
            bootstrap_servers=settings.BOOTSTRAP_SERVERS,
            value_deserializer=lambda message: json.loads(
                message.decode("utf-8"),
            ),
            *args,
            **kwargs,
        )
