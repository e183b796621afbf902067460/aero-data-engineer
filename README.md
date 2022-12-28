# DeFi Bachelor Thesis
Depends on: [defi-head-core](https://github.com/e183b796621afbf902067460/defi-head-core), [defi-web3](https://github.com/e183b796621afbf902067460/defi-web3), [defi-traders-composite](https://github.com/e183b796621afbf902067460/defi-traders-composite), [defi-providers-fabric](https://github.com/e183b796621afbf902067460/defi-providers-fabric) and [defi-overviews-fabric](https://github.com/e183b796621afbf902067460/defi-overviews-fabric).

---

# Configuration

First of all to configure DeFi Management project correctly need to do next steps:

- Clone current repository:
```
git clone https://github.com/e183b796621afbf902067460/defi-bachelor-thesis.git
```

- Get into the project folder:
```
cd defi-bachelor-thesis/
```

- Set the __ENV__ variables in `docker-compose.yaml`:
  
  - Providers environment variables in [airflow-common-env](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L50) service, by default:
 
    ```
    ETH_HTTP_PROVIDER: https://rpc.ankr.com/eth
    BSC_HTTP_PROVIDER: https://rpc.ankr.com/bsc
    AVAX_HTTP_PROVIDER: https://rpc.ankr.com/avalanche
    ARB_HTTP_PROVIDER: https://rpc.ankr.com/arbitrum
    FTM_HTTP_PROVIDER: https://rpc.ankr.com/fantom
    MATIC_HTTP_PROVIDER: https://rpc.ankr.com/polygon
    OPT_HTTP_PROVIDER: https://rpc.ankr.com/optimism
    ```

  - ClickHouse environment variables in [airflow-common-env](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L50) service, by default:
    ```
    CLICKHOUSE_HOST: clickhouse
    CLICKHOUSE_DB: defi_management
    CLICKHOUSE_USER: defi_management
    CLICKHOUSE_DEFAULT_ACCESS_MANAGEMENT: 1
    CLICKHOUSE_PASSWORD: defi_management
    ```
  - PostgreSQL environment variables in [airflow-common-env](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L50) service, by default:
    ```
    POSTGRES_HOST: orm
    POSTGRES_USER: defi_management
    POSTGRES_PASSWORD: defi_management
    POSTGRES_DB: defi_management
    ```
  
  - Back-end environment variables in [fastapi](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L117) service, by default:
    ```
    SERVER_HOST: 0.0.0.0
    SERVER_PORT: 8000
    ```
  - Front-end environment variables in [fastapi](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L117) service, by default:
    ```
    REACT_HOST: frontend
    REACT_PORT: 3000
    ```
  - Back-end environment variables in [react](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L103) service, by default:
    ```
    FASTAPI_HOST: fastapi
    FASTAPI_PORT: 8000
    ```
  - Set CORS in [settings.py](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/defi-fastapi/src/cfg/settings.py) to allow [frontend](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/tree/master/defi-react), by default:
    ```python
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        f"http://0.0.0.0:3000"
    ]
    ```
  - Set CORS in [axios.js](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/defi-react/src/services/axios.js) to allow [backend](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/tree/master/defi-fastapi), by default:
    ```js
    const baseURL = "http://0.0.0.0:8000/api/v1/";
    ```


# Docker

- Run docker commands (`sudo`):
```
docker build -t defi_airflow defi-airflow/
```

- Compose:
```
docker-compose up airflow-init
```

- Then:
```
docker-compose up -d
```

# Services

`Apache Airflow` at [http://0.0.0.0:8080](http://0.0.0.0:8080), by default:
  
  - Username:
    - airflow
  - Password:
    - airflow
 
`FastAPI` at [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs).

`ReactJS` at [http://0.0.0.0:3000](http://0.0.0.0:3000).

# Fixtures

Additional fixtures can be added to check project's success rate.

- See existing containers:
```
docker ps
```

- Copy `fastapi's` \<CONTAINER ID> and run inside of it:
```
docker exec -it <CONTAINER ID> pytest _fixtures/conftest.py
```

__By__ __default:__

- Username
```
defi_management
```
- Password
```
defi_management
```
- Chains
`ETH`, `BSC`, `FTM`, `AVAX`.
- Protocols
`Aave`, `Curve`, `UniSwap`, `SushiSwap`, `PancakeSwap`, `Convex`, `Geist`, `Nereus`, `Ellipsis`,  `Sturdy`.
- Yields
`Lending`, `Staking`, `Farming`, `DEX`.

# Exit
- To stop all running containers:
```
docker stop $(docker ps -a -q)
```
- And remove it all:
```
docker rm $(docker ps -a -q)
```
