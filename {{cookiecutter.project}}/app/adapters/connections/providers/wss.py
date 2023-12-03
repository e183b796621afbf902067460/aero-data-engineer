from raffaelo.providers.wss.provider import WSSProvider

from app.settings import settings


class WSSProviderConnection(WSSProvider):
    address, is_reverse = None, None

    def __init__(self):
        WSSProvider.__init__(self, uri=settings.WSS_NODE_PROVIDER)

