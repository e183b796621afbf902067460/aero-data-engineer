from dependency_injector import containers, providers

from app.services.quickswap_v3.service import QuickSwapV3HTTPService, QuickSwapV3WSSService
from app.settings import settings


class QuickSwapV3ServiceContainer(containers.DeclarativeContainer):
    """Container class for managing services related to QuickSwap V3.

    This container provides singleton instances of QuickSwapV3WSSService
    and QuickSwapV3HTTPService, configured with the provided address and
    reverse settings from the application's settings.

    Attributes
    ----------
        quickswap_v3_wss_service (providers.Singleton): Singleton provider
            for QuickSwapV3WSSService instance, configured with the provided
            address and reverse settings.
        quickswap_v3_http_service (providers.Singleton): Singleton provider
            for QuickSwapV3HTTPService instance, configured with the provided
            address and reverse settings.
    """

    quickswap_v3_wss_service = providers.Singleton(
        QuickSwapV3WSSService,
        address=settings.ADDRESS,
        is_reverse=settings.IS_REVERSE,
    )

    quickswap_v3_http_service = providers.Singleton(
        QuickSwapV3HTTPService,
        address=settings.ADDRESS,
        is_reverse=settings.IS_REVERSE,
    )
