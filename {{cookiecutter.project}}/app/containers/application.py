from dependency_injector import containers, providers

from app.containers.kafka.container import AIOKafkaContainer
from app.containers.quickswap_v3.container import QuickSwapV3ServiceContainer


class ApplicationContainer(containers.DeclarativeContainer):
    """Container class for managing the application's dependencies.

    This container aggregates other containers such as AIOKafkaContainer
    and QuickSwapV3ServiceContainer to provide a centralized point for
    managing the application's dependencies.

    Attributes
    ----------
        kafka_container (providers.Container): Container provider for
            AIOKafkaContainer instance, managing connections to Apache Kafka.
        quickswap_v3_container (providers.Container): Container provider for
            QuickSwapV3ServiceContainer instance, managing services related
            to QuickSwap V3.
    """

    kafka_container = providers.Container(
        AIOKafkaContainer,
    )

    quickswap_v3_container = providers.Container(
        QuickSwapV3ServiceContainer,
    )
