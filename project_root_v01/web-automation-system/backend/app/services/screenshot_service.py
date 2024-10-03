import logging

class ScreenshotService:
    def capture_screenshot(self, id, url, width=0, height=0):
        logging.info(f"Taking screenshot of {url}")
        # Implement screenshot logic here
        logging.info(f"Screenshot of {url} captured successfully")
        return {"id": id, "status": "success", "message": "Screenshot captured successfully"}
