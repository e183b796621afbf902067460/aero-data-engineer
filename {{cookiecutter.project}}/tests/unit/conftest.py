import pytest

from app.settings import settings

# TODO import particular service and repository
try:
    from app.adapters.repositories.abstract import iRepository  # noqa: F401
    from app.services.abstract import iService  # noqa: F401

    raise ImportError
except ImportError:
    ...


# TODO implement particular websocket service initialization and type hints
@pytest.fixture(scope="package")
def wss_service() -> iService:  # noqa: D103
    return iService(address=settings.ADDRESS, is_reverse=False)


# TODO implement particular websocket service and repository type hints
@pytest.fixture(scope="package")
def wss_repository(wss_service: iService) -> iRepository:  # noqa: D103
    return wss_service._repository
