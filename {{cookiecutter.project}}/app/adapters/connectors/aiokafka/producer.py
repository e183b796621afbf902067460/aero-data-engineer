from json import dumps

from aiokafka import AIOKafkaProducer

from app.settings import settings


class AIOKafkaProducerConnector(AIOKafkaProducer):

    def __init__(self, *args, **kwargs):
        AIOKafkaProducer.__init__(
            self,
            bootstrap_servers=[settings.BOOTSTRAP_SERVERS],
            value_serializer=lambda x: dumps(x).encode('utf-8'),
            *args, **kwargs
        )
