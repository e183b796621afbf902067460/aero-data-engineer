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
pipx run cookiecutter gh:e183b796621afbf902067460/quickview-template
```

# Update Files

- Move project's files to the root:
```bash
bash {{cookiecutter.project}}/docker-entrypoint-initdb.d/docker-entrypoint-initdb.sh
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
