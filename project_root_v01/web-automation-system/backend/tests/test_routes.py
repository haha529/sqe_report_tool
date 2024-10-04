import unittest
from unittest.mock import patch, mock_open, MagicMock
from fastapi.testclient import TestClient

from app.routes import router
from app.models import ScreenshotRequest, EmailRequest, TemplateRequest

client = TestClient(router)

class TestRoutes(unittest.TestCase):

    @patch("os.listdir", return_value=["template1.html", "template2.html"])
    def test_get_templates_success(self, mock_listdir):
        response = client.get("/templates")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"templates": ["template1.html", "template2.html"]})

    @patch("os.listdir", side_effect=Exception("Error"))
    def test_get_templates_failure(self, mock_listdir):
        response = client.get("/templates")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"detail": "Error"})

    @patch("builtins.open", new_callable=mock_open, read_data="template content")
    @patch("os.path.join", return_value="path/to/template1.html")
    def test_get_template_success(self, mock_path_join, mock_file):
        response = client.get("/template/template1.html")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"content": "template content"})

    @patch("builtins.open", side_effect=Exception("Error"))
    @patch("os.path.join", return_value="path/to/template1.html")
    def test_get_template_failure(self, mock_path_join, mock_file):
        response = client.get("/template/template1.html")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"detail": "Error"})

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.join", return_value="path/to/template1.html")
    def test_save_template_success(self, mock_path_join, mock_file):
        request_data = {"content": "new content"}
        response = client.post("/template/template1.html", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Template saved successfully"})

    @patch("builtins.open", side_effect=Exception("Error"))
    @patch("os.path.join", return_value="path/to/template1.html")
    def test_save_template_failure(self, mock_path_join, mock_file):
        request_data = {"content": "new content"}
        response = client.post("/template/template1.html", json=request_data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"detail": "Error"})

    @patch("app.services.screenshot_service.ScreenshotService.capture_screenshot", return_value={"id": 1, "url": "http://example.com"})
    def test_screenshot_success(self, mock_capture_screenshot):
        request_data = {"screenshots": [{"id": 1, "url": "http://example.com", "width": 800, "height": 600}]}
        response = client.post("/screenshot", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Screenshots taken", "results": [{"id": 1, "url": "http://example.com"}]})

    @patch("app.services.screenshot_service.ScreenshotService.capture_screenshot", side_effect=Exception("Error"))
    def test_screenshot_failure(self, mock_capture_screenshot):
        request_data = {"screenshots": [{"id": 1, "url": "http://example.com", "width": 800, "height": 600}]}
        response = client.post("/screenshot", json=request_data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"detail": "Error"})

    @patch("app.services.email_service.EmailService.send_email", return_value={"status": "success"})
    def test_email_success(self, mock_send_email):
        request_data = {"template": "template.html", "recipient": "test@example.com", "images": ["image1.png"], "custom_text": "Hello"}
        response = client.post("/send-email", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Emails sent", "results": {"status": "success"}})

    @patch("app.services.email_service.EmailService.send_email", side_effect=Exception("Error"))
    def test_email_failure(self, mock_send_email):
        request_data = {"template": "template.html", "recipient": "test@example.com", "images": ["image1.png"], "custom_text": "Hello"}
        response = client.post("/send-email", json=request_data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"detail": "Error"})

if __name__ == '__main__':
    unittest.main()