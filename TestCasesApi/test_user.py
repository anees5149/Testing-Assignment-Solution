import json
import unittest
import requests



class Test_forms(unittest.TestCase):
    def test(self):
        r = requests.get('http://127.0.0.1:8000/user')
        
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main() 