from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from abc import ABC
from typing import final


class iResource(ABC):

    DB_ADDRESS: str = None
    DB_PORT: int = None
    DB_USER: str = None
    DB_PASSWORD: str = None
    DB_NAME: str = None

    DB_URL: str = None

    @final
    def _db_uri(self) -> str:
        return self.DB_URL

    @final
    def get_engine(self) -> Engine:
        return create_engine(self._db_uri())
