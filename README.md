# quickview-template
A cookiecutter template to quickly create a streaming service with standardized project structure.

# Before Quickstart

- Create particular repository and clone it:
```bash
git clone https://github.com/{{cookiecutter.username}}/{{cookiecutter.project}}
```

- Change directory to this particular one:
```bash
cd {{cookiecutter.project}}
```

# Quickstart

- Install `pipx` because it is strongly recommended to use with `cookiecutter`:
```bash
pip3 install pipx  # 1.3.3
```

- Install `cookiecutter` using `pipx` previously installed:
```bash
pipx install cookiecutter  # 2.5.0
```

- Generate streaming project based on current template:
```bash
pipx run cookiecutter gh:e183b796621afbf902067460/cookiecutter-streaming-template
```

# Update Files

- Move `README.md`, `docker-compose.yaml`, `.gitignore` and `.pre-commit-config.yaml` to the root of the project:
```bash
bash {{cookiecutter.project}}/scripts/mv.sh
```

# Push

- Add changes to VCS:
```bash
git add .
```

- Commit it:
```bash
git commit -m "Cloned project structure via cookiecutter"
```

- And push:
```bash
git push
```
