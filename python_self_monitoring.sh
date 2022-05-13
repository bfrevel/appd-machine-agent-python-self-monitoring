#!/bin/bash

if [ ! -d ".venv" ]; then
    echo "install python3"
    apt-get install -y python3-venv

    echo "install virtual env"
    python3 -m venv .venv

    echo "activate venv and install requirements"
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "activate venv"
    source .venv/bin/activate 
fi

while [ 1 ]; do
    python self_monitoring.py
    sleep 60
done
