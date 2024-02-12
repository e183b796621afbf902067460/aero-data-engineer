from contextlib import asynccontextmanager

from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI

from app.adapters.connections.kafka.producer import AIOKafkaProducerConnection
from app.containers.application import ApplicationContainer
from app.services.quickswap_v3.service import QuickSwapV3WSSService
from app.views.abstract import publish


@asynccontextmanager
@inject
async def lifespan(
    app: FastAPI,
    service: QuickSwapV3WSSService = Provide[ApplicationContainer.quickswap_v3_container.quickswap_v3_wss_service],
    kafka: AIOKafkaProducerConnection = Provide[ApplicationContainer.kafka_container.kafka_producer_connection],
    *args,
    **kwargs,
) -> None:
    """Async context manager for managing the lifespan of services during application startup and shutdown.

    This function is an async context manager intended to be used during application startup
    and shutdown to manage the lifespan of services such as QuickSwap V3 WebSocket service and
    Kafka producer connection. It ensures that the required services are initialized and cleaned
    up properly.

    Args:
    ----
        app (FastAPI): The FastAPI application instance.
        service (QuickSwapV3WSSService, optional): The QuickSwap V3 WebSocket service.
            Defaults to Provide[ApplicationContainer.quickswap_v3_container.quickswap_v3_wss_service].
        kafka (AIOKafkaProducerConnection, optional): The Kafka producer connection.
            Defaults to Provide[ApplicationContainer.kafka_container.kafka_producer_connection].
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.

    Yields:
    ------
        None: The context manager yields None after executing the code block inside it.
    """

    await publish(service=service, kafka=kafka)
    yield
