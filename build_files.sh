#!/bin/bash

echo "BUILD START"

# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
    echo "ERROR: requirements.txt not found!"
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
python3 -m pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

# Check if staticfiles_build is created
if [ -d "staticfiles_build" ]; then
    echo "staticfiles_build directory exists."
else
    echo "ERROR: staticfiles_build directory does not exist."
    exit 1  # Exit with an error if the directory does not exist
fi

echo "BUILD END"
