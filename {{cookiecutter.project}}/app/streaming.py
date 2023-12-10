import asyncio

from fastkafka import FastKafka

from app.adapters.connections.kafka.producer import AIOKafkaProducerConnection
from app.schemas.transactions.schema import TransactionsBatch
from app.settings import settings


class FastKafkaApp(FastKafka):
    """FastKafkaApp extends FastKafka to provide a customized Kafka application.

    Note:
    ----
        This class sets default values for certain FastKafka parameters
        to simplify the initialization process.
    """

    def __init__(self, *args, **kwargs):
        FastKafka.__init__(
            self,
            kafka_brokers={
                settings.KAFKA_BROKER_URL: {
                    "url": settings.KAFKA_BROKER_URL,
                    "port": settings.KAFKA_BROKER_PORT,
                },
            },
            bootstrap_servers_id=[settings.BOOTSTRAP_SERVERS],
            *args,
            **kwargs,
        )

    @staticmethod
    async def to_clickhouse(producer: AIOKafkaProducerConnection, events: TransactionsBatch) -> None:
        """Asynchronously send real-time transactions to ClickHouse integrated with Kafka engine.

        Args:
        ----
            producer (AIOKafkaProducerConnection): A Kafka producer connection.
            events (TransactionsBatch): Batch of real-time transactions events.

        Returns:
        -------
            None

        Note:
        ----
            This method uses the provided Kafka producer to send each transaction series
            in the provided batch to the Kafka topic.
        """
        await asyncio.gather(
            *(
                producer.send(topic=settings.TOPIC_NAME, value=dict(series))
                for series in events.q_real_time_tx_processing_series
            ),
        ) if events.q_real_time_tx_processing_series else ...


fastkafka_app = FastKafkaApp()
