import unittest
from app.models import Screenshot

class TestScreenshotModel(unittest.TestCase):
    def test_screenshot_creation(self):
        request_id = 1
        url = "https://example.com"
        image_path = "path/to/image.png"
        screenshot = Screenshot(request_id, url, image_path)
        self.assertEqual(screenshot.url, url)
        self.assertEqual(screenshot.image_path, image_path)
        self.assertEqual(screenshot.id, request_id)

if __name__ == "__main__":
    unittest.main()