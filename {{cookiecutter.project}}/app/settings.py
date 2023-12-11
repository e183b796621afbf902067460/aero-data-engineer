import os
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from app.utils import strtobool

load_dotenv()


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

    BOOTSTRAP_SERVERS: Optional[str] = os.getenv("BOOTSTRAP_SERVERS", None)
    KAFKA_BROKER_URL: Optional[str] = os.getenv("KAFKA_BROKER_URL", None)
    KAFKA_BROKER_PORT: Optional[int] = os.getenv("KAFKA_BROKER_PORT", None)
    TOPIC_NAME: Optional[str] = os.getenv("TOPIC_NAME", None)

    WSS_NODE_PROVIDER: Optional[str] = os.getenv("WSS_NODE_PROVIDER", None)


settings = Settings()
