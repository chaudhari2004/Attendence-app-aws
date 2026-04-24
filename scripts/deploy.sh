#!/bin/bash

cd /home/ubuntu/backend

# Stop old app
pkill -f app.py

# Install dependencies
pip install -r requirements.txt

# Start app
nohup python3 app.py &
