import asyncio

from app.adapters.connections.kafka.producer import AIOKafkaProducerConnection
from app.schemas.transactions.schema import TransactionsBatch
from app.settings import settings

INFINITY = iter(int, 1)


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


def strtobool(value: str) -> bool:
    """Convert a string representing a boolean value to an integer.

    Args:
    ----
        value (str): The string value to be converted.

    Returns:
    -------
        int: 1 if the value is truthy, 0 if it's falsy.

    Raises:
    ------
        ValueError: If the provided string does not represent a valid boolean value.
    """
    value = value.lower()
    if value in ("y", "yes", "t", "true", "on", "1"):
        return True
    elif value in ("n", "no", "f", "false", "off", "0"):
        return False
    raise ValueError(f"Invalid truth value {value}.")
