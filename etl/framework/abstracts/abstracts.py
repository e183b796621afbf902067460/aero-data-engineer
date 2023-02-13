from abc import ABC
from typing import final

from framework.fabrics.pit_users.fabrics import usersEndpointFabric


class SourceAbstractFabric(ABC):

    def __init__(self) -> None:
        self._fabrics: dict = dict()

    @final
    def add_fabric(self, fabric_name: str, fabric) -> None:
        if not self._fabrics.get(fabric_name):
            self._fabrics[fabric_name] = fabric

    @final
    def get_fabric(self, fabric_name: str):
        fabric = self._fabrics.get(fabric_name)
        if not fabric:
            raise ValueError(f'Set Fabric for {fabric_name} fabric type')
        return fabric


sourceAbstractFabric = SourceAbstractFabric()

sourceAbstractFabric.add_fabric(fabric_name='users', fabric=usersEndpointFabric)
