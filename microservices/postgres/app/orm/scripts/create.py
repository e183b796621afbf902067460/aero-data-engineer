from app.orm.cfg.engine import ORMEngine

from sqlalchemy_utils import database_exists, drop_database, create_database


if __name__ == '__main__':
    ENGINE = ORMEngine.get_engine()
    URI = ORMEngine.get_uri()

    if database_exists(URI):
        drop_database(URI)
    create_database(URI)
