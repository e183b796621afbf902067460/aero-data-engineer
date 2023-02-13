import os


class AeroUsersEndpointHandler:

    def __init__(self) -> None:
        self._pit_users: dict = dict()

    @property
    def pit_users(self):
        return self._pit_users

    def _parse(self, json_: dict, prefix: str = 'pit_') -> None:
        for k, v in json_.items():
            if isinstance(v, dict):
                self._parse(json_=v, prefix=f'{prefix}{k}_')
            if not isinstance(v, dict):
                self.pit_users[prefix + k] = v

    def do(self, json_: dict):
        self._parse(json_=json_)


