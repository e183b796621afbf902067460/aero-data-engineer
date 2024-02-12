from dependency_injector import containers, providers

from app.adapters.connections.kafka.consumer import AIOKafkaConsumerConnection
from app.adapters.connections.kafka.producer import AIOKafkaProducerConnection


class AIOKafkaContainer(containers.DeclarativeContainer):
    """Container class for managing connections to Apache Kafka using async IO.

    This container provides singleton instances of AIOKafkaProducerConnection
    and AIOKafkaConsumerConnection, allowing for easy management and injection
    of Kafka connections throughout the application.

    Attributes
    ----------
        kafka_producer_connection (providers.Singleton): Singleton provider
            for AIOKafkaProducerConnection instance.
        kafka_consumer_connection (providers.Singleton): Singleton provider
            for AIOKafkaConsumerConnection instance.
    """

    kafka_producer_connection = providers.Singleton(
        AIOKafkaProducerConnection,
    )

    kafka_consumer_connection = providers.Singleton(
        AIOKafkaConsumerConnection,
    )
