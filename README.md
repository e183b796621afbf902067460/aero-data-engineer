# cookiecutter-quickview-template
A cookiecutter template to quickly create a streaming service with standardized project structure.

# Before Quickstart

- Create particular repository and clone it:
```bash
git clone https://github.com/e183b796621afbf902067460/{{cookiecutter.project}}
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

- Move `README.md` to the root of the project:
```bash
mv {{cookiecutter.project}}/README.md ./README.md
```

- Move `.gitignore`:
```bash
mv {{cookiecutter.project}}/.gitignore ./.gitignore
```

- Also move `_clickhouse/`:
```bash
mv {{cookiecutter.project}}/_clickhouse ./_clickhouse
```

- And `docker-compose.yaml`:
```bash
mv {{cookiecutter.project}}/docker-compose.yaml ./docker-compose.yaml
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
