import pytest
from raffaelo.contracts.erc20.contract import ERC20TokenContract

# TODO import particular repository
try:
    from app.adapters.repositories.abstract import iRepository  # noqa: F401

    raise ImportError
except ImportError:
    ...


# TODO implement particular websocket repository type hints
@pytest.mark.repositories
def test__wss_repository__token0__must_be_erc20(wss_repository: iRepository):  # noqa: D103
    assert isinstance(wss_repository._token0, ERC20TokenContract)


# TODO implement particular websocket repository type hints
@pytest.mark.repositories
def test__wss_repository__token1__must_be_erc20(wss_repository: iRepository):  # noqa: D103
    assert isinstance(wss_repository._token1, ERC20TokenContract)
