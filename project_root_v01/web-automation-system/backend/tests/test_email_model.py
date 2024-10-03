import unittest
from app.models import Email

class TestEmailModel(unittest.TestCase):
    def test_email_creation(self):
        email = Email(recipient="test@example.com", subject="Test Subject", body="Test Body")
        self.assertEqual(email.recipient, "test@example.com")
        self.assertEqual(email.subject, "Test Subject")
        self.assertEqual(email.body, "Test Body")

if __name__ == "__main__":
    unittest.main()