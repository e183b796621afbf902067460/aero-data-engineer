# {{cookiecutter.project}}
A cookiecutter-based project to stream data from [liquidity pool](https://{{cookiecutter.blockchain}}/address/{{cookiecutter.address}}).

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

- Change directory where `pyprject.toml` is located:
```bash
cd {{cookiecutter.project}}/
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

<p><small>Based on <a target="_blank" href="https://github.com/e183b796621afbf902067460/quickview-template">quickview-template</a>.</small></p>
