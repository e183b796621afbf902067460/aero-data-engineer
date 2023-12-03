from raffaelo.providers.http.provider import HTTPProvider

from app.settings import settings


class HTTPProviderConnection(HTTPProvider):
    address, is_reverse = None, None

    def __init__(self):
        HTTPProvider.__init__(self, uri=settings.WSS_NODE_PROVIDER)
