# {{cookiecutter.project}}

[![license](https://img.shields.io/:license-Apache%202-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)
[![code-style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A cookiecutter-based project to stream data from [liquidity pool](https://{{cookiecutter.blockchain}}/address/{{cookiecutter.address}}).

# Configuration

- Clone current repository:
```bash
git clone https://github.com/{{cookiecutter.username}}/{{cookiecutter.project}}.git
```

- Get into the project folder:
```bash
cd {{cookiecutter.project}}/
```

- Set `WSS_NODE_PROVIDER` environment variable in [docker-compose.yaml](https://github.com/{{cookiecutter.username}}/{{cookiecutter.project}}/blob/master/docker-compose.yaml).

# Quickstart

- Create `venv` and activate it:
```bash
python3 -m venv venv && source venv/bin/activate
```

# Dependency Management
Project's dependencies are managed by the [poetry](https://python-poetry.org/).
Moving to poetry has helped to have `pyproject.toml` as a single configuration file for the whole project as well.

- Install `poetry`:
```bash
pip3 install poetry  # 1.7.1
```

- And install project's dependencies:
```bash
poetry install --no-root
```

# Add New Dependency

- If a new dependency have to be added, then it can be done this way, for example to add `fastapi`:
```bash
poetry add fastapi
```

- And lock it:
```bash
poetry lock --no-update
```

# How To Use Pre-Commit Hooks

[`pre-commit`](https://pre-commit.com/) is used to run pre-commit hooks.
All configurations are in the `.pre-commit-config.yaml`.
To run commands below all dependencies have to be installed.

- To initialize hook:
```bash
pre-commit install
```

- To check all files, not only files in the commit:
```bash
pre-commit run --all-files
```

# Configuration

### Kafka environment variables

- `BOOTSTRAP_SERVERS`: Kafka application bootstrap servers.
- `TOPIC_NAME`: Kafka application topic name.

### Node environment variables

- `WSS_NODE_PROVIDER`: WebSocket node provider.

# Deploy

- Run all in docker, perhaps using `sudo`:
```bash
docker-compose up -d --build --force-recreate
```

- Check [`KafkaUI`](http://0.0.0.0:8080/) streaming data.

- Stop all services:
```bash
docker-compose down -v
```

<p><small>Based on <a target="_blank" href="https://github.com/e183b796621afbf902067460/quickview-template">quickview-template</a>.</small></p>
