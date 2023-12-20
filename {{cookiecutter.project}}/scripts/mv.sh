#!/bin/bash

echo "Moving core files to project's root $(pwd)/."

mv ./{{cookiecutter.project}}/.gitignore $(pwd)/
mv ./{{cookiecutter.project}}/.pre-commit-config.yaml $(pwd)/
mv ./{{cookiecutter.project}}/docker-compose.yaml $(pwd)/
mv ./{{cookiecutter.project}}/README.md $(pwd)/
mv ./{{cookiecutter.project}}/.github $(pwd)/
mv ./{{cookiecutter.project}}/_clickhouse $(pwd)/
