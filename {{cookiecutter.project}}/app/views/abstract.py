import asyncio
import sys

from loguru import logger

from app.adapters.connections.kafka.producer import AIOKafkaProducerConnection
from app.schemas.transactions.schema import TransactionsBatch
from app.services.abstract import iService
from app.settings import settings
from app.utils import INFINITY, to_clickhouse


@logger.catch(onerror=lambda _: sys.exit(1))
async def publish(service: iService, kafka: AIOKafkaProducerConnection):
    """Asynchronously broadcasts transactions from a specified liquidity pool to ClickHouse via Kafka.

    This function initializes a Kafka producer connection using AIOKafkaProducerConnection,
    and starts the connection. It then enters an infinite loop where it observes transactions
    from a specified liquidity pool using a service implementing the iService interface.

    The function gathers asynchronous tasks for sending batches of transactions to ClickHouse
    via the initialized Kafka producer. The transactions are obtained from the observed events
    provided by the specified service.

    Raises
    ------
    - SystemExit: Exits the program with code 1 in case of an error during logging.

    Note:
    ----
    - The INFINITY constant is used to create an infinite loop for continuously observing
      transactions.
    """
    await kafka.start()

    logger.info(f"Service for {settings.ADDRESS} on {settings.BLOCKCHAIN} started.")

    for _ in INFINITY:
        await asyncio.gather(
            *(
                to_clickhouse(producer=kafka, events=TransactionsBatch.from_iterable(events))
                for events in service.observe(blockchain=settings.BLOCKCHAIN)
            ),
        )
