#!/bin/bash

project=$(dirname "$(dirname "$(pwd)")")

echo "Moving core files to project's root $project"

mv ../.gitignore $project/
mv ../.pre-commit-config.yaml $project/
mv ../docker-compose.yaml $project/
mv ../README.md $project/
