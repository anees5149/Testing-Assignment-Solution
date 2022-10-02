import requests
import unittest

class Test_forms(unittest.TestCase):
    def test(self):
        r = requests.post('http://127.0.0.1:8000/answers/', json={
            "user_id": 1,
            "answers": [
                {
                "question_id":2,
                "alternative_id": 3
                }
            ]
            })
        print(f"Status Code: {r.status_code}, Response: {r.json()}")

        self.assertEqual(r.status_code, 201)

if __name__ == '__main__':
    unittest.main() 