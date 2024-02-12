from fastapi import FastAPI

from app.containers.application import ApplicationContainer

container = ApplicationContainer()
container.wire(modules=[__name__])

# TODO import particular lifespan function
app = FastAPI(lifespan=...)
app.container = container


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="__main__:app", host="0.0.0.0")
