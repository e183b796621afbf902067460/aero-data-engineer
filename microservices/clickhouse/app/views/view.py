from fastapi import FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from app.cfg.settings import settings


app = FastAPI()
router = InferringRouter()


@cbv(router=router)
class ClickhouseCBV:
    ...


app.include_router(router=router, prefix=f'{settings.API_V1}' + '/clickhouse')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='view:app', host='0.0.0.0')
