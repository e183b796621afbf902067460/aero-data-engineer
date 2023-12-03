from json import loads

from aiokafka import AIOKafkaConsumer

from app.settings import settings


class AIOKafkaConsumerConnector(AIOKafkaConsumer):

    def __init__(self, *args, **kwargs):
        AIOKafkaConsumer.__init__(
            self,
            bootstrap_servers=[settings.BOOTSTRAP_SERVERS],
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            *args, **kwargs
        )



