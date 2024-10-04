import unittest
from unittest.mock import patch, MagicMock
from PIL import Image
from app.utils.image_utils import resize_image

class TestImageUtils(unittest.TestCase):

    @patch("app.utils.image_utils.Image.open")
    def test_resize_image_with_given_dimensions(self, mock_open):
        mock_img = MagicMock()
        mock_open.return_value = mock_img
        mock_img.size = (800, 600)

        result = resize_image("path/to/image.jpg", width=400, height=300)

        self.assertEqual(result, "path/to/image_resized.jpg")

    @patch("app.utils.image_utils.Image.open")
    def test_resize_image_with_only_width(self, mock_open):
        mock_img = MagicMock()
        mock_open.return_value = mock_img
        mock_img.size = (800, 600)

        result = resize_image("path/to/image.jpg", width=400)

        self.assertEqual(result, "path/to/image_resized.jpg")

    @patch("app.utils.image_utils.Image.open")
    def test_resize_image_with_only_height(self, mock_open):
        mock_img = MagicMock()
        mock_open.return_value = mock_img
        mock_img.size = (800, 600)

        result = resize_image("path/to/image.jpg", height=300)

        self.assertEqual(result, "path/to/image_resized.jpg")

    @patch("app.utils.image_utils.Image.open")
    def test_resize_image_with_no_dimensions(self, mock_open):
        mock_img = MagicMock()
        mock_open.return_value = mock_img
        mock_img.size = (800, 600)

        result = resize_image("path/to/image.jpg")

        self.assertEqual(result, "path/to/image_resized.jpg")

    @patch("app.utils.image_utils.Image.open")
    def test_resize_image_with_invalid_path(self, mock_open):
        mock_open.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            resize_image("invalid/path/to/image.jpg")

if __name__ == '__main__':
    unittest.main()