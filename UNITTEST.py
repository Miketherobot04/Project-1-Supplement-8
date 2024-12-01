import unittest
from unittest.mock import patch
Test Cases
python
Copy code
class TestHTTPRequests(unittest.TestCase):

    @patch('requests.get')
    def test_send_get_request_json(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"key": "value"}'
        mock_get.return_value.headers = {"Content-Type": "application/json"}
        result = send_get_request("http://example.com")
        self.assertEqual(result, {"key": "value"})

    @patch('requests.get')
    def test_send_get_request_non_json(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "Hello World"
        mock_get.return_value.headers = {"Content-Type": "text/plain"}
        result = send_get_request("http://example.com")
        self.assertEqual(result, (200, "Hello World"))

    @patch('requests.get')
    def test_get_echo_response(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.headers = {
            "Postman-Token": "test-token",
            "X-Forwarded-For": "127.0.0.1"
        }
        token, ip = get_echo_response()
        self.assertEqual(token, "test-token")
        self.assertEqual(ip, "127.0.0.1")

    @patch('requests.post')
    def test_post_hello_world(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"success": true}'
        mock_post.return_value.headers = {"Content-Type": "application/json"}
        result = post_hello_world()
        self.assertEqual(result, {"success": True})