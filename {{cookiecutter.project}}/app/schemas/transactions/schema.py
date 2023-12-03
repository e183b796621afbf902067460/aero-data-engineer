import typing

from pydantic import BaseModel
from typing import Iterable


class _TransactionSeries(BaseModel):

    q_real_time_tx_processing_blockchain: str
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
        return cls(**{k: v for k, v in zip(cls.model_fields.keys(), iterable)})


class TransactionsBatch(BaseModel):
    q_real_time_tx_processing_series: typing.List[_TransactionSeries]

    @classmethod
    def from_iterable(cls, iterable: Iterable):
        return cls(**{key: [_TransactionSeries.from_iterable(value) for value in iterable] for key in cls.model_fields.keys()})
