import unittest
from unittest.mock import patch, mock_open

from app.services.email_service import EmailService
from app.utils.logging_config import setup_logging

setup_logging()

class TestEmailService(unittest.TestCase):
    def test_send_email(self):
        service = EmailService()
        recipient = "test@example.com"
        template_name = "email_template.html"
        images = []
        custom_text = ""
        result = service.send_email(template_name, recipient, images, custom_text)
        self.assertTrue(result["status"] == "success")
        self.assertTrue(result["message"] == "Email sent successfully")

    @patch("builtins.open", new_callable=mock_open, read_data="Hello, {{ custom_text }}")
    @patch("os.path.join", return_value="path/to/template.html")
    def test_get_email_body_with_custom_text(self, mock_path_join, mock_file):
        email_service = EmailService()
        email_body = email_service.get_email_body("Custom Text", ["image1.png"], "template.html")
        self.assertIn("Custom Text", email_body)


    @patch("builtins.open", new_callable=mock_open, read_data="Hello, {{ custom_text }}")
    @patch("os.path.join", return_value="path/to/template.html")
    def test_get_email_body_template_not_found(self, mock_path_join, mock_file):
        mock_file.side_effect = FileNotFoundError
        email_service = EmailService()
        with self.assertRaises(FileNotFoundError):
            email_service.get_email_body("Custom Text", ["image1.png"], "nonexistent_template.html")
if __name__ == "__main__":
    unittest.main()