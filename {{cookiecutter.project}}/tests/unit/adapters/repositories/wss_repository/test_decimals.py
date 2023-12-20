import pytest

# TODO import particular repository
try:
    from app.adapters.repositories.abstract import iRepository  # noqa: F401

    raise ImportError
except ImportError:
    ...


# TODO implement particular websocket repository type hints
@pytest.mark.unit
def test__wss_repository__token0_decimals__must_be_int(wss_repository: iRepository):  # noqa: D103
    assert isinstance(wss_repository._token0_decimals, int)


# TODO implement particular websocket repository type hints
@pytest.mark.unit
def test__wss_repository__token1_decimals__must_be_int(wss_repository: iRepository):  # noqa: D103
    assert isinstance(wss_repository._token1_decimals, int)


# TODO implement particular websocket repository type hints and fill to_ option
@pytest.mark.unit
def test__wss_repository__token0_decimals__must_be_equal_to_(wss_repository: iRepository):  # noqa: D103
    assert wss_repository._token0_decimals == ...


# TODO implement particular websocket repository type hints and fill to_ option
@pytest.mark.unit
def test__wss_repository__token1_decimals__must_be_equal_to_(wss_repository: iRepository):  # noqa: D103
    assert wss_repository._token1_decimals == ...
