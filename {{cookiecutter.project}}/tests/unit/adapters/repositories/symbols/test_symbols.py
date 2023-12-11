import pytest

# TODO import particular repository
try:
    from app.adapters.repositories.abstract import iRepository

    raise ImportError
except ImportError:
    ...


# TODO implement particular websocket repository type hints
@pytest.mark.repositories
def test__wss_repository__token0_symbol__must_be_str(wss_repository: iRepository):  # noqa: D103
    assert isinstance(wss_repository._token0_symbol, str)


# TODO implement particular websocket repository type hints
@pytest.mark.repositories
def test__wss_repository__token1_symbol__must_be_str(wss_repository: iRepository):  # noqa: D103
    assert isinstance(wss_repository._token1_symbol, str)


# TODO implement particular websocket repository type hints and fill to_ option
@pytest.mark.repositories
def test__wss_repository__token0_symbol__must_be_equal_to_(wss_repository: iRepository):  # noqa: D103
    assert wss_repository._token0_symbol == ...


# TODO implement particular websocket repository type hints and fill to_ option
@pytest.mark.repositories
def test__wss_repository__token1_symbol__must_be_equal_to_(wss_repository: iRepository):  # noqa: D103
    assert wss_repository._token1_symbol == ...
