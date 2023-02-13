from framework.handlers.pit_users.aero.handlers import AeroUsersEndpointHandler


class UsersEndpointFabric:

    def __init__(self):
        self._handlers: dict = dict()

    @property
    def handlers(self):
        return self._handlers

    def add_handler(self, source: str, handler) -> None:
        if not self.handlers.get(source):
            self.handlers[source] = handler

    def get_handler(self, source: str):
        handler = self.handlers.get(source)
        if not handler:
            raise ValueError(f'Set UsersEndpointHandler handler for {source}')
        return handler


usersEndpointFabric = UsersEndpointFabric()

usersEndpointFabric.add_handler(source='aero', handler=AeroUsersEndpointHandler())
