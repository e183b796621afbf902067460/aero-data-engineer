from fastapi import FastAPI

from app.observer import observer
from app.settings import settings
from app.streaming import fastkafka_app


@fastkafka_app.run_in_background()
async def _():
    await observer()


fastapi_app = FastAPI(lifespan=fastkafka_app.fastapi_lifespan(kafka_broker_name=settings.KAFKA_BROKER_URL))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="__main__:fastapi_app", host="0.0.0.0")
