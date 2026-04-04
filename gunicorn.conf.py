# gunicorn.conf.py
# Arian Nasr
# April 4, 2026

import os


BIND_ADDRESS = os.environ.get('BIND_ADDRESS', '0.0.0.0')
BIND_PORT = int(os.environ.get('BIND_PORT', 5001))

bind = f"{BIND_ADDRESS}:{BIND_PORT}"
workers = 2
accesslog = "-" # Log to stdout
errorlog = "-"  # Log to stderr

# gunicorn -c gunicorn.conf.py main:app