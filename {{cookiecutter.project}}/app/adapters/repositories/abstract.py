from abc import ABC

from app.adapters.connections.providers.http import HTTPProviderConnection
from app.adapters.connections.providers.wss import WSSProviderConnection


class iRepository(ABC):
    """iRepository is an abstract base class (ABC) representing a generic repository interface.

    Attributes:
    ----------
        _provider: Placeholder for a provider to connect to blockchain node.
        _protocol: Placeholder for a particular DeFi protocol.

    Note:
    ----
        This class is intended to be subclassed to create concrete repository interfaces.
    """

    _provider: WSSProviderConnection | HTTPProviderConnection
    _protocol: str
