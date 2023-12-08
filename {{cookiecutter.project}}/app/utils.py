from typing import Any, Callable

INFINITY = iter(int, 1)


def initialize_class(cls: type) -> object:
    """Initialize a class by creating an instance with default constructor.

    Args:
    ----
        cls (Type): The class to be initialized.

    Returns:
    -------
        object: An instance of the provided class.
    """
    return cls()


def call_function(fn: Callable) -> Any:
    """Call a provided function and return its result.

    Args:
    ----
        fn (Callable): The function to be called.

    Returns:
    -------
        Any: The result of calling the provided function.
    """
    return fn()


async def call_async_function(fn: Callable) -> Any:
    """Call a provided asynchronous function and return its result.

    Args:
    ----
        fn (Callable): The function to be called.

    Returns:
    -------
        Any: The result of calling the provided function.
    """
    return await fn()


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
