FROM apache/airflow:2.4.1

USER root

RUN apt-get update && apt-get install -y git

USER airflow

ENV ETH_HTTP_PROVIDER="https://rpc.ankr.com/eth"
ENV BSC_HTTP_PROVIDER="https://rpc.ankr.com/bsc"
ENV AVAX_HTTP_PROVIDER="https://rpc.ankr.com/avalanche"
ENV ARB_HTTP_PROVIDER="https://rpc.ankr.com/arbitrum"
ENV FTM_HTTP_PROVIDER="https://rpc.ankr.com/fantom"
ENV MATIC_HTTP_PROVIDER="https://rpc.ankr.com/polygon"
ENV OPT_HTTP_PROVIDER="https://rpc.ankr.com/optimism"

RUN pip install clickhouse-sqlalchemy
RUN pip install clickhouse-driver

RUN pip install git+https://github.com/e183b796621afbf902067460/defi-head-core.git#egg=defi-head-core
RUN pip install git+https://github.com/e183b796621afbf902067460/defi-web3.git#egg=defi-web3
RUN pip install git+https://github.com/e183b796621afbf902067460/defi-providers-fabric.git#egg=defi-providers-fabric
RUN pip install git+https://github.com/e183b796621afbf902067460/defi-traders-composite.git#egg=defi-traders-composite
RUN pip install git+https://github.com/e183b796621afbf902067460/defi-overviews-fabric.git#egg=defi-overviews-fabric
