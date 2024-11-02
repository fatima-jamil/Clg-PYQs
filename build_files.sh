#!/bin/bash

echo "BUILD START"

# Install dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput --clear

# Check if staticfiles_build is created
if [ -d "staticfiles_build" ]; then
    echo "staticfiles_build directory exists."
else
    echo "staticfiles_build directory does not exist."
    exit 1  # Exit with an error if the directory does not exist
fi

echo "BUILD END"
