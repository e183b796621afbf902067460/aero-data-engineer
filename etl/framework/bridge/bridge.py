from typing import final
from framework.abstracts.abstracts import SourceAbstractFabric


class Bridge:

    def __init__(self, abstract: SourceAbstractFabric, fabric_name: str, handler_name: str) -> None:
        self._abstract = abstract
        self._fabric_name = fabric_name
        self._handler_name = handler_name

    @property
    def abstract(self):
        return self._abstract

    @final
    def produce_fabric(self):
        return self.abstract.get_fabric(self._fabric_name)

    @final
    def produce_handler(self):
        return self.produce_fabric().get_handler(self._handler_name)
