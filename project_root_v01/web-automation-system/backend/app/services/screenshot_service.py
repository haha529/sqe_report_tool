import base64
import json
import logging
import os

from app import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

class ScreenshotService:
    def __init__(self):
        self.screenshot_jsonfile = config.get_screenshot_file()
        self.screenshot_dir = config.get_screenshot_dir()


    def capture_screenshot(self, id, url, width=0, height=0):
        logging.info(f"Taking screenshot of {url}")

        # Save screenshot to file
        file_path = os.path.join(self.screenshot_dir, f"{id}.png")
        with open(file_path, 'wb') as file:
            file.write(self.take_screenshot(url, width, height))

        # crop image if width and height are provided
        cropped_file_path = os.path.join(self.screenshot_dir, f"{id}_cropped.png")
        if width and height:
            image = Image.open(cropped_file_path)
            image = image.crop((0, 0, width, height))
            image.save(cropped_file_path)
        else:
            cropped_file_path = file_path

        # Return base64 string
        with open(cropped_file_path, 'rb') as file:
            base64_string = base64.b64encode(file.read()).decode('utf-8')
        logging.info(f"Screenshot of {url} captured successfully")
        return {"id": id, "url": url, "base64_image": base64_string}


    def get_screenshots(self):
        if not os.path.exists(self.screenshot_jsonfile):
            return "No screenshots available"

        with open(self.screenshot_jsonfile, 'r') as file:
            screenshots = json.load(file)

        logging.info(f"Retrieved {len(screenshots)} screenshots")
        return json.dump(screenshots, indent=4)


    def take_screenshot(self, url, window_width=1900, window_height=8000):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            driver.set_window_size(window_width, window_height)
            driver.get(url)
            screenshot = driver.get_screenshot_as_png()
        finally:
            driver.quit()

        return screenshot
