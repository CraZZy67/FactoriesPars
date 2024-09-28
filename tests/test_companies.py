import unittest
from company_links import Companies

class TestCompanies(unittest.TestCase):
    def setUp(self):
        headers = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        }
        