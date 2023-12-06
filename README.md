# cookiecutter-streaming-template
A cookiecutter-based template to quickly create a project for a streaming service with standardized project structure.

# Before Quickstart

- Create particular repository and clone it:
```bash
git clone https://github.com/e183b796621afbf902067460/streaming-service-etherscan.io-0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640.git
```

- Create `venv`:
```bash
python3 -m venv venv
```

- And activate it:
```bash
source venv/bin/activate
```

# Quickstart

- Install `pipx` because it is strongly recommended to use with `cookiecutter`:
```bash
pip3 install pipx
```

- Install `cookiecutter` using `pipx` previously installed:
```bash
pipx install cookiecutter
```

- Generate streaming project based on current template:
```bash
pipx run cookiecutter gh:e183b796621afbf902067460/cookiecutter-streaming-template
```
