#!/bin/bash

# Navigate to your project directory
cd /home/ubuntu/rock-paper-scissor

# Stash any local changes
git stash

# Pull the latest changes from the main branch
git pull origin main

# Check if there are any conflicts
if git status | grep -q "Unmerged paths"; then
    # If there are conflicts, exit with an error message
    echo "Error: There are unresolved merge conflicts."
    exit 1
fi

# Activate your Python virtual environment (if applicable)
source ../env/bin/activate

cd /home/ubuntu/rock-paper-scissor/backend
# Install/update Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Migration
python manage.py migrate

# Restart Gunicorn or any other services if necessary
sudo systemctl restart gunicorn

sudo systemctl restart nginx
