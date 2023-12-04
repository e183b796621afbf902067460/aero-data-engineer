from raffaelo.providers.wss.provider import WSSProvider

from app.settings import settings


class WSSProviderConnection(WSSProvider):
    """WSSProviderConnection extends WSSProvider to establish a connection
    to a WebSocket Secure (WSS) provider with the specified URI.

    Note:
    ----
        This class initializes the WSSProvider with default values,
        setting the URI to the value specified in the 'WSS_NODE_PROVIDER'
        setting from the application settings.
    """

    def __init__(self):
        WSSProvider.__init__(self, uri=settings.WSS_NODE_PROVIDER)
