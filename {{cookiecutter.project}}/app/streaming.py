from fastkafka import FastKafka

from app.settings import settings
from app.utils import initialize_class


class FastKafkaApp(FastKafka):

    def __init__(self, *args, **kwargs):
        FastKafka.__init__(
            self,
            kafka_brokers={
                settings.KAFKA_BROKER_URL: {
                    "url": settings.KAFKA_BROKER_URL,
                    "port": settings.KAFKA_BROKER_PORT
                }
            },
            bootstrap_servers_id=[settings.BOOTSTRAP_SERVERS],
            *args, **kwargs
        )


fastkafka_app = initialize_class(FastKafkaApp)