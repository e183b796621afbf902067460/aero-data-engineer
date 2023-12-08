import os
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from app.utils import call_function, initialize_class, strtobool

call_function(load_dotenv)


class Settings(BaseSettings):
    """Settings represents the configuration settings for the application.

    Attributes:
    ----------
        APP_NAME (str): The name of the application.
        BLOCKCHAIN (str): The blockchain used by the application.
        ADDRESS (str): The address used by the application.

        IS_DEVELOPMENT (bool): Flag indicating whether the application is in development mode.

        BOOTSTRAP_SERVERS (str): Kafka bootstrap servers for messaging.
        KAFKA_BROKER_URL (str): URL of the Kafka broker.
        KAFKA_BROKER_PORT (int): Port of the Kafka broker.
        TOPIC_NAME (str): Topic name.

        WSS_NODE_PROVIDER (Optional[str]): WebSocket Secure (WSS) node provider URI.
        HTTP_NODE_PROVIDER (Optional[str]): HTTP node provider URI.

    Note:
    ----
        Default values for some attributes are retrieved from environment variables
        or specified values, including values provided during project generation
        using the 'cookiecutter' tool.
    """

    APP_NAME: str = "{{cookiecutter.project}}"
    BLOCKCHAIN: str = "{{cookiecutter.blockchain}}"
    ADDRESS: str = "{{cookiecutter.address}}"

    IS_DEVELOPMENT: bool = bool(
        strtobool(os.getenv("IS_DEVELOPMENT", "False")),
    )

    BOOTSTRAP_SERVERS: str
    KAFKA_BROKER_URL: str
    KAFKA_BROKER_PORT: int
    TOPIC_NAME: str

    WSS_NODE_PROVIDER: Optional[str] = None
    HTTP_NODE_PROVIDER: Optional[str] = None


settings = initialize_class(Settings)
