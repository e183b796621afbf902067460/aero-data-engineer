from typing import Iterable, List

from pydantic import BaseModel


class _TransactionSeries(BaseModel):
    """_TransactionSeries represents a series of real-time transaction processing data."""

    q_real_time_tx_processing_blockchain: str
    q_real_time_tx_processing_protocol: str
    q_real_time_tx_processing_address: str
    q_real_time_tx_processing_swap_maker: str
    q_real_time_tx_processing_t0_symbol: str
    q_real_time_tx_processing_t1_symbol: str
    q_real_time_tx_processing_t0_amount: float
    q_real_time_tx_processing_t1_amount: float
    q_real_time_tx_processing_tx_hash: str
    q_real_time_tx_processing_timestamp: str

    @classmethod
    def from_iterable(cls, iterable: Iterable):
        """Create an instance of _TransactionSeries from an iterable object.

        Args:
        ----
            iterable (Iterable): An iterable containing values corresponding
                to the attributes of _TransactionSeries.

        Returns:
        -------
            _TransactionSeries: An instance of _TransactionSeries.
        """
        return cls(**{key: value for key, value in zip(cls.model_fields.keys(), iterable)})


class TransactionsBatch(BaseModel):
    """TransactionsBatch represents a batch of real-time transaction processing data."""

    q_real_time_tx_processing_series: List[_TransactionSeries]

    @classmethod
    def from_iterable(cls, iterable: Iterable):
        """Create an instance of TransactionsBatch from an iterable.

        Args:
        ----
            iterable (Iterable): An iterable containing values corresponding
                to the attributes of TransactionsBatch.

        Returns:
        -------
            TransactionsBatch: An instance of TransactionsBatch.
        """
        return cls(
            **{key: [_TransactionSeries.from_iterable(value) for value in iterable] for key in cls.model_fields.keys()},
        )
