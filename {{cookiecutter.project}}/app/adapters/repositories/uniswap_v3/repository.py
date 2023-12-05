from raffaelo_uniswap_v3.pool.contract import UniSwapV3PoolContract
from web3 import Web3
from web3.middleware import geth_poa_middleware

from app.adapters.connections.providers.http import HTTPProviderConnection
from app.adapters.connections.providers.wss import WSSProviderConnection
from app.adapters.repositories.abstract import iRepository
from app.utils import initialize_class


class UniSwapV3WSSRepository(iRepository):
    """UniSwapV3WSSRepository represents a repository for interacting with UniSwap V3 contracts
    using WebSocket Secure (WSS) connection.

    Attributes:
    ----------
        _provider (Type): The connection provider type (WSSProviderConnection).
        _contract (UniSwapV3PoolContract): An instance of UniSwapV3PoolContract for the specified address.
        _token0, _token1: Instances of ERC20 tokens representing the pair tokens.
        _token0_symbol, _token1_symbol: Symbols of the pair tokens.
        _token0_decimals, _token1_decimals: Decimals of the pair tokens.
        _blocks: A filter for Swap events in the UniSwap contract.
        _w3: Web3 instance connected to the specified node.

    Args:
    ----
        address (str): The UniSwap V3 contract address.
        is_reverse (bool): Flag indicating the token order in the pair.

    Note:
    ----
        This class extends the iRepository abstract class.
    """

    _provider = WSSProviderConnection

    def __init__(self, address: str, is_reverse: bool) -> None:
        self._contract: UniSwapV3PoolContract = UniSwapV3PoolContract(
            address=Web3.to_checksum_address(value=address),
            provider=initialize_class(self._provider),
        )

        self._token0, self._token1 = (
            self._contract.token0() if not is_reverse else self._contract.token1(),
            self._contract.token1() if not is_reverse else self._contract.token0(),
        )
        self._token0_symbol, self._token1_symbol = self._token0.symbol(), self._token1.symbol()
        self._token0_decimals, self._token1_decimals = self._token0.decimals(), self._token1.decimals()

        self._blocks = self._contract.contract.events.Swap.create_filter(
            fromBlock="latest",
        )

        self._w3 = Web3(self._contract.node)
        self._w3.middleware_onion.inject(
            geth_poa_middleware,
            layer=0,
        )


class UniSwapV3HTTPRepository(UniSwapV3WSSRepository):
    """UniSwapV3HTTPRepository represents a repository for interacting with UniSwap V3 contracts
    using HTTP connection.

    Attributes:
    ----------
        _provider (Type): The connection provider type (HTTPProviderConnection).

    Note:
    ----
        This class inherits from UniSwapV3WSSRepository class.
    """

    _provider = HTTPProviderConnection
