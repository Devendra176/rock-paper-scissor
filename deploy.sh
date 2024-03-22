#!/bin/bash

# Navigate to your project directory
cd /home/ubuntu/rock-paper-scissor

git stash 

# Pull the latest changes from the main branch and merge them
git pull --no-rebase origin main

# Activate your Python virtual environment (if applicable)
source ../env/bin/activate

# Install/update Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

cd /home/ubuntu/rock-paper-scissor/backend

# Migration
python manage.py migrate

# Restart Gunicorn or any other services if necessary
sudo systemctl restart gunicorn

sudo systemctl restart nginx

# Changes
