from app.orm.base import hSources
from app.orm.base import hEndpoints

from app.orm.base import lSourcesEndpoints

from app.orm.cfg.engine import ORMEngine


if __name__ == "__main__":
    session = ORMEngine.get_session()

    h_source = hSources(h_source='aero')
    h_endpoint = hEndpoints(h_endpoint='https://random-data-api.com/api/v2/users')

    session.add_all([h_source, h_endpoint])
    session.commit()

    l_source_endpoint = lSourcesEndpoints(
        h_source_id=h_source.h_source_id,
        h_endpoint_id=h_endpoint.h_endpoint_id
    )

    session.add(l_source_endpoint)
    session.commit()
