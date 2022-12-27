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
  
  - Providers environment variables in [airflow-worker](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L220) service, by default:
 
    ```
    ETH_HTTP_PROVIDER: https://rpc.ankr.com/eth
    BSC_HTTP_PROVIDER: https://rpc.ankr.com/bsc
    AVAX_HTTP_PROVIDER: https://rpc.ankr.com/avalanche
    ARB_HTTP_PROVIDER: https://rpc.ankr.com/arbitrum
    FTM_HTTP_PROVIDER: https://rpc.ankr.com/fantom
    MATIC_HTTP_PROVIDER: https://rpc.ankr.com/polygon
    OPT_HTTP_PROVIDER: https://rpc.ankr.com/optimism
    ```

  - ClickHouse environment variables in [airflow-worker](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L220) service, by default:
    ```
    CLICKHOUSE_ADDRESS: clickhouse
    CLICKHOUSE_DB: defi_management
    CLICKHOUSE_USER: defi_management
    CLICKHOUSE_PASSWORD: defi_management
    ```
  - PostgreSQL environment variables in [airflow-worker](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L220) service, by default:
    ```
    POSTGRES_ADDRESS: orm
    POSTGRES_USER: defi_management
    POSTGRES_PASSWORD: defi_management
    POSTGRES_DB: defi_management
    ```
  - PostgreSQL environment variables in [postgres](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L157) service, by default:
    ```
    POSTGRES_USER: airflow
    POSTGRES_PASSWORD: airflow
    POSTGRES_DB: airflow
    ```
  - ClickHouse environment variables in [clickhouse](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L139) service, by default:
    ```
    CLICKHOUSE_HOST: clickhouse
    CLICKHOUSE_DB: defi_management
    CLICKHOUSE_USER: defi_management
    CLICKHOUSE_DEFAULT_ACCESS_MANAGEMENT: 1
    CLICKHOUSE_PASSWORD: defi_management
    ```
  - PostgreSQL environment variables in [orm](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L122) service, by default:
    ```
    POSTGRES_HOST: orm
    POSTGRES_USER: defi_management
    POSTGRES_PASSWORD: defi_management
    POSTGRES_DB: defi_management
    ```
  - PostgreSQL environment variables in [fastapi](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L96) service, by default:
    ```
    DB_ADDRESS: orm
    DB_NAME: defi_management
    DB_USER: defi_management
    DB_PASSWORD: defi_management
    ```
  - Back-end environment variables in [fastapi](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L96) service, by default:
    ```
    SERVER_HOST: 0.0.0.0
    SERVER_PORT: 8000
    ```
  - Front-end environment variables in [fastapi](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L96) service, by default:
    ```
    REACT_HOST: frontend
    REACT_PORT: 3000
    ```
  - Back-end environment variables in [react](https://github.com/e183b796621afbf902067460/defi-bachelor-thesis/blob/master/docker-compose.yaml#L82) service, by default:
    ```
    FASTAPI_HOST: fastapi
    FASTAPI_PORT: 8000
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

# Exit
- To stop all running containers:
```
docker stop $(docker ps -a -q)
```
- And remove it all:
```
docker rm $(docker ps -a -q)
```
