#!flask/bin/python
import unittest

from requests import get


class TestCase(unittest.TestCase):

    def test_get_fashins(self):
        response = get('http://localhost:5000/api/fashin')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content, '[]')

    def test_get_fashins_empty(self):
        response = get('http://localhost:5000/api/fashin?page=10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '[]')

    def test_get_fashins_specify_page_limit_empty(self):
        response = get('http://localhost:5000/api/fashin?page=10&limit=30')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '[]')

    def test_get_fashins_specify_page_limit(self):
        response = get('http://localhost:5000/api/fashin?page=2&limit=30')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content, '[]')

if __name__ == '__main__':
    unittest.main()