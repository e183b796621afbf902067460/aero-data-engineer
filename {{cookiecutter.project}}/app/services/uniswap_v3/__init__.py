def _amount0(is_reverse: bool, a0, a1, d0, d1) -> float:
    if not is_reverse:
        amount0 = a0 / 10**d0
    else:
        amount0 = a1 / 10**d1

    return amount0
