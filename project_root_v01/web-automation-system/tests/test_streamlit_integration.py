import unittest
from streamlit.testing.v1 import AppTest

from frontend import app

@unittest.skip("Skip Streamlit tests")
class TestStreamlitIntegration(unittest.TestCase):
    def setUp(self):
        self.client = StreamlitTestClient()
        self.client.start(app)

    def test_streamlit_interface(self):
        # Test the Streamlit interface for URL input and screenshot capture
        response = self.client.post("/", data={"url": "http://example.com"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Screenshot captured", response.data.decode())

        # Test the Streamlit interface for email sending
        response = self.client.post("/send-email", data={
            "recipient": "test@example.com",
            "subject": "Test Email",
            "body": "This is a test email.",
            "attachments": ["path/to/screenshot.png"]
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Email sent successfully", response.data.decode())

if __name__ == "__main__":
    unittest.main()