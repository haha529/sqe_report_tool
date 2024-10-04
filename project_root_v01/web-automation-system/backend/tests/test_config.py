import unittest
from unittest.mock import patch, MagicMock
import os
import logging
from app.config import get_templates_dir

class TestConfig(unittest.TestCase):

    @patch("os.path.abspath", return_value="/path/to/dir/app/config.py")
    @patch("logging.info")
    def test_templates_dir_correct_path(self, mock_logging_info, mock_os_path_abspath):
        @patch("os.path.abspath", return_value="/path/to/dir/app/config.py")
        def test_linux(self, mock_os_path_abspath):
            result = get_templates_dir()
            self.assertEqual(result, "/path/to/dir/app/templates")
        @patch("os.path.abspath", return_value="\\path\\to\\dir\\app\\config.py")
        def test_windows(self, mock_os_path_abspath):
            result = get_templates_dir()
            self.assertEqual(result, "\\path\\to\\dir\\app\\templates")

        if os.name == 'nt':
            test_windows()
        else:
            test_linux()

if __name__ == '__main__':
    unittest.main()