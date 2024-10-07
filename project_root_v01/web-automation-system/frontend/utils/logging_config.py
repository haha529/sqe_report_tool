import logging
import logging.config
import os

# Ensure the log directory exists
log_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../log')
os.makedirs(log_directory, exist_ok=True)

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(log_directory, 'app.log'),
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)