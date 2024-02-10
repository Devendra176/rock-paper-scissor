#!/bin/bash

# Install necessary packages
sudo apt-get update
sudo apt-get install -y python3 python3-pip git gunicorn

# Clone the GitHub repository
git clone https://github.com/Devendra176/rock-paper-scissor.git /home/ubuntu

# Change directory to your Django project
cd /home/ubuntu/rock-paper-scissor/backend/

# Install Python dependencies
pip3 install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Restart Gunicorn server
sudo systemctl restart gunicorn
