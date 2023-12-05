import asyncio
import sys

from app.adapters.connections.kafka.producer import AIOKafkaProducerConnection
from app.adapters.connections.logger.handler import log
from app.schemas.transactions.schema import TransactionsBatch
from app.services.abstract import iService
from app.settings import settings
from app.streaming import FastKafkaApp
from app.utils import INFINITY, initialize_class

try:
    from app.adapters.repositories.uniswap_v3.repository import UniSwapV3WSSRepository  # noqa: F401
except ImportError:
    ...


@log.catch(onerror=lambda _: sys.exit(1))
async def broadcast() -> None:
    """Asynchronously broadcasts transactions from a specified liquidity pool to ClickHouse via Kafka.

    This function initializes a Kafka producer connection using AIOKafkaProducerConnection,
    and starts the connection. It then enters an infinite loop where it observes transactions
    from a specified liquidity pool using a service implementing the iService interface, such as
    UniSwapV3WSSRepository.

    The function gathers asynchronous tasks for sending batches of transactions to ClickHouse
    via the initialized Kafka producer. The transactions are obtained from the observed events
    provided by the specified service.

    Raises
    ------
    - SystemExit: Exits the program with code 1 in case of an error during logging.

    TODOs:
    - Specify a particular liquidity pool reverse parameter based on the trading pair.
    - Implement using a particular service from app.services.

    Note:
    ----
    - The INFINITY constant is used to create an infinite loop for continuously observing
      transactions.
    """
    # TODO Specify particular liquidity pool reverse parameter based on trading pair
    is_reverse: bool = ...  # True of False
    # TODO Implement using particular service from app.services
    service: iService = ...  # UniSwapV3WSSRepository(address=settings.ADDRESS, is_reverse=is_reverse)

    kafka = initialize_class(AIOKafkaProducerConnection)
    await kafka.start()

    for _ in INFINITY:
        await asyncio.gather(
            *(
                FastKafkaApp.to_clickhouse(producer=kafka, events=TransactionsBatch.from_iterable(events))
                for events in service.observe(blockchain=settings.BLOCKCHAIN, is_reverse=is_reverse)
            ),
        )
