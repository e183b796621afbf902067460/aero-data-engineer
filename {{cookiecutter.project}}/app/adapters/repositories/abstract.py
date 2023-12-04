from abc import ABC


class iRepository(ABC):
    """iRepository is an abstract base class (ABC) representing a generic repository interface.

    Attributes:
    ----------
        address: Placeholder for the repository address.
        is_reverse: Placeholder for a boolean indicating reverse status.

    Note:
    ----
        This class is intended to be subclassed to create concrete repository interfaces.
    """

    address, is_reverse = None, None
