from app.orm.cfg.engine import ORMEngine
from app.orm.base.main import Base

from sqlalchemy_utils import database_exists

if __name__ == '__main__':
    ENGINE, URI = ORMEngine.get_engine(), ORMEngine.get_uri()

    if database_exists(URI):
        Base.metadata.drop_all(ENGINE)
