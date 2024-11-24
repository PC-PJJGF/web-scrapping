import unittest
from scraper.scraper import get_html

class TestWebScraping(unittest.TestCase):
    def test_get_html_success(self):
        url = "https://www.example.com"
        result = get_html(url)
        self.assertIsNotNone(result)

    def test_get_html_invalid_url(self):
        url = "https://invalid-url.com"
        result = get_html(url)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
