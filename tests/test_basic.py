import unittest
from app import app

class TestBasicFunctionality(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_injection_endpoint(self):
        response = self.app.get('/injection/search?username=test')
        self.assertEqual(response.status_code, 200)
