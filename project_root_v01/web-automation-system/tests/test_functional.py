import unittest
from fastapi.testclient import TestClient
from app.main import app
import os

class TestFunctional(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_screenshot_and_email_functionality(self):
        # Test screenshot capture
        response = self.client.post("/screenshot", json={"url": "http://example.com"})
        self.assertEqual(response.status_code, 200)
        screenshot_path = response.json().get("screenshot_path")
        self.assertTrue(screenshot_path.endswith(".png"))
        self.assertTrue(os.path.exists(screenshot_path))

        # Test email sending
        response = self.client.post("/send-email", json={
            "recipient": "test@example.com",
            "subject": "Test Email",
            "body": "This is a test email.",
            "attachments": [screenshot_path]
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get("success"))

        # Clean up
        os.remove(screenshot_path)

if __name__ == "__main__":
    unittest.main()