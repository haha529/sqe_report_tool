import unittest
from app.services.screenshot_service import ScreenshotService
from app.utils.logging_config import setup_logging

setup_logging()

class TestScreenshotService(unittest.TestCase):
    def test_capture_screenshot(self):
        service = ScreenshotService()
        url = "https://example.com"
        request_id = 0
        result = service.capture_screenshot(request_id, url)
        self.assertTrue(result["id"] == request_id)
        self.assertTrue(result["status"] == "success")
        self.assertTrue(result["message"] == "Screenshot captured successfully")

if __name__ == "__main__":
    unittest.main()