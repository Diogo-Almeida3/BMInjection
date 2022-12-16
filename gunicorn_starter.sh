#!/bin/sh
echo "Starting..."
gunicorn app:app -b 0.0.0.0:8000 -e PYTHONUNBUFFERED=1 