#!/bin/bash

echo "Moving core files to project's root $(pwd)/."

# Function to move and check
standardize() {
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
standardize "./{{cookiecutter.project}}/.github" "$(pwd)/"

# Move app to $(pwd)
standardize "./{{cookiecutter.project}}/app" "$(pwd)/"

# Move images to $(pwd)
standardize "./{{cookiecutter.project}}/images" "$(pwd)/"

# Move tests to $(pwd)
standardize "./{{cookiecutter.project}}/tests" "$(pwd)/"

# Move .gitignore to $(pwd)
standardize "./{{cookiecutter.project}}/.gitignore" "$(pwd)/"

# Move .pre-commit-config.yaml to $(pwd)
standardize "./{{cookiecutter.project}}/.pre-commit-config.yaml" "$(pwd)/"

# Move docker-compose.yaml to $(pwd)
standardize "./{{cookiecutter.project}}/docker-compose.yaml" "$(pwd)/"

# Move Dockerfile to $(pwd)
standardize "./{{cookiecutter.project}}/Dockerfile" "$(pwd)/"

# Move LICENSE to $(pwd)
standardize "./{{cookiecutter.project}}/LICENSE" "$(pwd)/"

# Move poetry.lock to $(pwd)
standardize "./{{cookiecutter.project}}/poetry.lock" "$(pwd)/"

# Move pyproject.toml to $(pwd)
standardize "./{{cookiecutter.project}}/pyproject.toml" "$(pwd)/"

# Move README.md to $(pwd)
standardize "./{{cookiecutter.project}}/README.md" "$(pwd)/"

# Remove {{cookiecutter.project}} directory
echo "Removing {{cookiecutter.project}} directory..."
rm -rf "{{cookiecutter.project}}"
if [ $? -eq 0 ]; then
    echo "{{cookiecutter.project}} directory removed successfully [x]."
else
    echo "Failed to remove {{cookiecutter.project}} directory [-]."
fi
