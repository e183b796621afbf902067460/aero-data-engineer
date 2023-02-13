from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr
from fastapi_utils.camelcase import camel2snake

from app.orm.base.main import Base


class lSourcesEndpoints(Base):

    @declared_attr
    def __tablename__(cls) -> str:
        return camel2snake(cls.__name__)

    l_source_endpoint_id = Column(Integer, primary_key=True)
    h_source_id = Column(Integer, ForeignKey('h_sources.h_source_id'), nullable=False)
    h_endpoint_id = Column(Integer, ForeignKey('h_endpoints.h_endpoint_id'), nullable=False)
    l_source_endpoint_load_ts = Column(DateTime, server_default=func.now(), nullable=False)
