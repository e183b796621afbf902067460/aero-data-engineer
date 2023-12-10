INFINITY = iter(int, 1)


def strtobool(value: str) -> int:
    """Convert a string representing a boolean value to an integer.

    Args:
    ----
        value (str): The string value to be converted.

    Returns:
    -------
        int: 1 if the value is truthy, 0 if it's falsy.

    Raises:
    ------
        ValueError: If the provided string does not represent a valid boolean value.
    """
    value = value.lower()
    if value in ("y", "yes", "t", "true", "on", "1"):
        return 1
    elif value in ("n", "no", "f", "false", "off", "0"):
        return 0
    else:
        raise ValueError(f"invalid truth value {value}")
