import unittest
from io import StringIO
import sys
import requests
# from website.setup import create_app
# from test_base import run_unittests
# from test_base import captured_io

class MyTestCase(unittest.TestCase):
    URL = "http://127.0.0.1:5000"

    # app = create_app()
    # app.run(debug=True)

    def test1(self):
        r = requests.get(MyTestCase.URL+"/login")
        self.assertEqual(r.status_code, 200)


    def test2(self):
        r = requests.get(MyTestCase.URL+"/logout")
        self.assertEqual(r.status_code, 200)


    def test3(self):
        r = requests.get(MyTestCase.URL+"/sign-up")
        self.assertEqual(r.status_code, 200)


    def test4(self):
        r = requests.get(MyTestCase.URL+"/")
        self.assertEqual(r.status_code, 200)


    def test5(self):
        r = requests.get(MyTestCase.URL+"/login")
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()