import logging
import os

def get_root_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_data_dir():
    data_dir = os.path.join(get_root_dir(), 'data')
    logging.info(f"Data directory: {data_dir}")
    return data_dir


def get_templates_dir():
    templates_dir = os.path.join(get_data_dir(), 'templates')
    logging.info(f"Templates directory: {templates_dir}")
    return templates_dir


def get_screenshot_dir():
    screenshot_dir = os.path.join(get_data_dir(), 'screenshots')
    logging.info(f"Screenshots directory: {screenshot_dir}")
    return screenshot_dir


def get_screenshot_file():
    screenshot_file = os.path.join(get_data_dir(), 'screenshots.json')
    logging.info(f"Screenshots file: {screenshot_file}")
    return screenshot_file