from abc import ABC, abstractmethod


class iService(ABC):
    """An abstract base class representing a generic service interface.

    Attributes
    ----------
    - _repository (type): The type of repository associated with the service.

    Methods
    -------
    - observe(*args, **kwargs): An abstract method to be implemented by subclasses for observing data.
    """

    _repository: type

    @abstractmethod
    def observe(self, *args, **kwargs):
        """An abstract method to be implemented by subclasses for observing data.

        Args:
        ----
        - *args, **kwargs: Additional arguments for observation.

        Raises:
        ------
        NotImplementedError: This method must be implemented by concrete subclasses.
        """
        raise NotImplementedError
