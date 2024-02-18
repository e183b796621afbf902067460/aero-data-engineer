import os
from typing import List, Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class _Settings(BaseSettings):
    """Settings represents the configuration settings for the application.

    Attributes:
    ----------
        APP_NAME (str): The name of the application.
        BLOCKCHAIN (str): The blockchain used by the application.
        ADDRESS (str): The address used by the application.
        IS_REVERSE (bool): The reverse parameter used by the application.

        BOOTSTRAP_SERVERS (str): Kafka bootstrap servers for messaging.
        TOPIC_NAME (str): Topic name.

        WSS_NODE_PROVIDER (Optional[str]): WebSocket Secure (WSS) node provider URI.

    Note:
    ----
        Default values for some attributes are retrieved from environment variables
        or specified values, including values provided during project generation
        using the 'cookiecutter' tool.
    """

    APP_NAME: str = "{{cookiecutter.project}}"
    BLOCKCHAIN: str = "{{cookiecutter.blockchain}}"
    ADDRESS: str = "{{cookiecutter.address}}"
    IS_REVERSE: bool = True if "{{cookiecutter.is_reverse}}".lower() in ["true", "t", "yes", "y", 1] else False

    BOOTSTRAP_SERVERS: List[str] = os.getenv("BOOTSTRAP_SERVERS", None).split(sep=',')
    TOPIC_NAME: Optional[str] = os.getenv("TOPIC_NAME", None)

    WSS_NODE_PROVIDER: Optional[str] = os.getenv("WSS_NODE_PROVIDER", None)


def _get_settings() -> _Settings:
    return _Settings()


settings: _Settings = _get_settings()
