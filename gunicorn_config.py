# gunicorn_config.py

# Server socket
bind = "0.0.0.0:8000"

# Worker processes
workers = 4
worker_class = "sync"  # Use "gevent" or "eventlet" for async
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50

# Timeouts
timeout = 120
keepalive = 5

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = "my-portfolio"

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL (if needed)
keyfile = "key.pem"
certfile = "cert.pem"