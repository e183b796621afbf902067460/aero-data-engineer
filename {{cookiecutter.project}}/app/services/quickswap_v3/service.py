import datetime
from typing import Iterable, List

from web3._utils.filters import LogReceipt

from app.adapters.repositories.quickswap_v3.repository import QuickSwapV3HTTPRepository, QuickSwapV3WSSRepository
from app.services.abstract import iService


class QuickSwapV3WSSService(iService):
    """A service class for observing QuickSwap V3 transactions through WebSocket.

    Attributes
    ----------
    - _repository (QuickSwapV3WSSRepository): The repository for interacting with QuickSwap V3 through WebSocket.

    Methods
    -------
    - observe(is_reverse: bool, blockchain: str, *args, **kwargs) -> List[Iterable].
    """

    _repository = QuickSwapV3WSSRepository

    def _amount0(self, swap: LogReceipt) -> float:
        """Calculate the adjusted amount0 based on the provided swap, repository, and reverse flag.

        Args:
        ----
        - is_reverse (bool): A flag indicating whether to reverse the calculation.
        - swap (LogReceipt): The swap object containing amount information.

        Returns:
        -------
        float: The calculated adjusted amount0.
        """
        if not self._is_reverse:
            amount0 = swap.args.amount0 / 10**self._repository._token0_decimals
        else:
            amount0 = swap.args.amount1 / 10**self._repository._token0_decimals
        return amount0

    def _amount1(self, swap: LogReceipt) -> float:
        """Calculate the adjusted amount1 based on the provided swap, repository, and reverse flag.

        Args:
        ----
        - is_reverse (bool): A flag indicating whether to reverse the calculation.
        - swap (LogReceipt): The swap object containing amount information.

        Returns:
        -------
        float: The calculated adjusted amount1.
        """
        if not self._is_reverse:
            amount1 = swap.args.amount1 / 10**self._repository._token1_decimals
        else:
            amount1 = swap.args.amount0 / 10**self._repository._token1_decimals
        return amount1

    def observe(self, blockchain: str, *args, **kwargs) -> List[Iterable]:
        """Observes UniSwap V3 transactions and yields relevant information.

        Args:
        ----
        - is_reverse (bool): A flag indicating whether to reverse the observation.
        - blockchain (str): The blockchain on which UniSwap V3 transactions are observed.
        - *args, **kwargs: Additional arguments for observation.

        Returns:
        -------
        List[Iterable]: A list of iterables containing transaction information.
        """
        yield [
            (
                blockchain,
                self._repository._protocol,
                self._repository._contract._address,
                swap.args.recipient,
                self._repository._token0_symbol,
                self._repository._token1_symbol,
                self._amount0(swap=swap),
                self._amount1(swap=swap),
                swap.transactionHash.hex(),
                str(
                    datetime.datetime.fromtimestamp(
                        int(self._repository._w3.eth.get_block(swap.blockNumber).timestamp),
                    ),
                ),
            )
            for swap in self._repository._blocks.get_new_entries()
        ]


class QuickSwapV3HTTPService(QuickSwapV3WSSRepository):
    """A service class for observing QuickSwap V3 transactions through HTTP.

    Attributes
    ----------
    - _repository (QuickSwapV3HTTPRepository): The repository for interacting with QuickSwap V3 through HTTP.

    Methods
    -------
    - observe(is_reverse: bool, blockchain: str, *args, **kwargs) -> List[Iterable].
    """

    _repository = QuickSwapV3HTTPRepository
