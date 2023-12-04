from raffaelo.providers.http.provider import HTTPProvider

from app.settings import settings


class HTTPProviderConnection(HTTPProvider):
    """HTTPProviderConnection extends HTTPProvider to establish a connection
    to a remote HTTP provider with the specified URI.

    Note:
    ----
        This class initializes the HTTPProvider with default values,
        setting the URI to the value specified in the 'WSS_NODE_PROVIDER'
        setting from the application settings.
    """

    def __init__(self):
        HTTPProvider.__init__(self, uri=settings.HTTP_NODE_PROVIDER)
