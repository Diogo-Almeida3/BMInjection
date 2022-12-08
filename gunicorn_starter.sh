echo "Starting"
gunicorn --chdir src main:app -b 0.0.0.0:8000