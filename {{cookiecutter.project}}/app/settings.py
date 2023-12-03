from distutils.util import strtobool
import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from app.utils import initialize_class, call_function


call_function(load_dotenv)


class Settings(BaseSettings):

    APP_NAME: str = "{{cookiecutter.project}}"
    BLOCKCHAIN: str = "{{cookiecutter.blockchain}}"
    ADDRESS: str = "{{cookiecutter.address}}"

    IS_DEVELOPMENT: bool = bool(strtobool(os.getenv('IS_DEVELOPMENT', 'False')))
    LOG_LEVEL: str = "INFO"

    BOOTSTRAP_SERVERS: str
    KAFKA_BROKER_URL: str
    KAFKA_BROKER_PORT: int

    WSS_PROVIDER: str

    class Config:
        env_file = ".env"


settings = initialize_class(Settings)  # type: ignore
