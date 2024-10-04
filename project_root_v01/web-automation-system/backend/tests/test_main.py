import unittest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

class TestMain(unittest.TestCase):
    def test_read_main(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to the Web Automation System!"}

if __name__ == "__main__":
    unittest.main()
