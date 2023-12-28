#!/bin/bash

echo "Moving core files to project's root $(pwd)/."

# Function to move and check
move_and_check() {
    src="$1"
    dest="$2"

    mv "$src" "$dest"
    if [ $? -eq 0 ]; then
        echo "$src moved successfully to $dest [x]."
    else
        echo "Failed to move $src to $dest [-]."
    fi
    echo
}

# Move .github to $(pwd)
move_and_check "./{{cookiecutter.project}}/.github" "$(pwd)/"

# Move app to $(pwd)
move_and_check "./{{cookiecutter.project}}/app" "$(pwd)/"

# Move images to $(pwd)
move_and_check "./{{cookiecutter.project}}/images" "$(pwd)/"

# Move tests to $(pwd)
move_and_check "./{{cookiecutter.project}}/tests" "$(pwd)/"

# Move .gitignore to $(pwd)
move_and_check "./{{cookiecutter.project}}/.gitignore" "$(pwd)/"

# Move .pre-commit-config.yaml to $(pwd)
move_and_check "./{{cookiecutter.project}}/.pre-commit-config.yaml" "$(pwd)/"

# Move docker-compose.yaml to $(pwd)
move_and_check "./{{cookiecutter.project}}/docker-compose.yaml" "$(pwd)/"

# Move Dockerfile to $(pwd)
move_and_check "./{{cookiecutter.project}}/Dockerfile" "$(pwd)/"

# Move LICENSE to $(pwd)
move_and_check "./{{cookiecutter.project}}/LICENSE" "$(pwd)/"

# Move poetry.lock to $(pwd)
move_and_check "./{{cookiecutter.project}}/poetry.lock" "$(pwd)/"

# Move pyproject.toml to $(pwd)
move_and_check "./{{cookiecutter.project}}/pyproject.toml" "$(pwd)/"

# Move README.md to $(pwd)
move_and_check "./{{cookiecutter.project}}/README.md" "$(pwd)/"

# Remove {{cookiecutter.project}} directory
echo "Removing {{cookiecutter.project}} directory..."
rm -rf "{{cookiecutter.project}}"
if [ $? -eq 0 ]; then
    echo "{{cookiecutter.project}} directory removed successfully [x]."
else
    echo "Failed to remove {{cookiecutter.project}} directory [-]."
fi
