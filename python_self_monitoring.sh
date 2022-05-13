#!/bin/bash

source .venv/bin/activate 

while [ 1 ]; do
    python self_monitoring.py
    sleep 60
done
