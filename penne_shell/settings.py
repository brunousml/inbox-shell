import os

FRONTDESK_HOST = os.environ.get('FRONT_DESK_HOST', '127.0.0.1:80')
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'guest@127.0.0.1:5672')
MONITORING_FOLDER = os.environ.get('MONITORING_FOLDER', '/home')
SAFE_MODE = os.environ.get('SAFE_MODE', True)
