import logging
import os

def get_templates_dir():
    templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info(f"Templates directory: {templates_dir}")
    return templates_dir