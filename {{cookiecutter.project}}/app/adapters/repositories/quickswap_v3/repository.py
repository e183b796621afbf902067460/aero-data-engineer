from raffaelo_quickswap_v3.pool.contract import QuickSwapV3AlgebraPoolContract
from web3 import Web3
from web3.middleware import geth_poa_middleware

from app.adapters.connections.providers.http import HTTPProviderConnection
from app.adapters.connections.providers.wss import WSSProviderConnection
from app.adapters.repositories.abstract import iRepository


class QuickSwapV3WSSRepository(iRepository):
    """QuickSwapV3WSSRepository represents a repository for interacting with QuickSwap V3 contracts
    using WebSocket Secure (WSS) connection.

    Attributes:
    ----------
        _provider (Type): The connection provider type (WSSProviderConnection).
        _protocol (str): Particular DeFi protocol of a contract.
        _contract (QuickSwapV3AlgebraPoolContract): An instance of QuickSwapV3AlgebraPoolContract.
        _token0, _token1: Instances of ERC20 tokens representing the pair tokens.
        _token0_symbol, _token1_symbol: Symbols of the pair tokens.
        _token0_decimals, _token1_decimals: Decimals of the pair tokens.
        _blocks: A filter for Swap events in the QuickSwap contract.
        _w3: Web3 instance connected to the specified node.

    Args:
    ----
        address (str): The QuickSwap V3 contract address.
        is_reverse (bool): Flag indicating the token order in the pair.

    Note:
    ----
        This class extends the iRepository abstract class.
    """

    _provider = WSSProviderConnection
    _protocol = "QuickSwap V3"

    def __init__(self, address: str, is_reverse: bool) -> None:
        self._contract: QuickSwapV3AlgebraPoolContract = QuickSwapV3AlgebraPoolContract(
            address=Web3.to_checksum_address(value=address),
            provider=self._provider(),
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


class QuickSwapV3HTTPRepository(QuickSwapV3WSSRepository):
    """QuickSwapV3HTTPRepository represents a repository for interacting with QuickSwap V3 contracts
    using HTTP connection.

    Attributes:
    ----------
        _provider (Type): The connection provider type (HTTPProviderConnection).

    Note:
    ----
        This class inherits from QuickSwapV3WSSRepository class.
    """

    _provider = HTTPProviderConnection
