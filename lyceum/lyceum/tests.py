from django.test import Client, TestCase
from django.conf import settings
import re


class StaticURLTests(TestCase):
    def test_middleware(self):
        tests = ["/about/", "/catalog/", "/coffee/", "/catalog/5/"]
        request = Client.get("/coffe/")
        for test in tests:
            for i in range(101):
                response = request.session.get(test)
                print(response.getvalue().decode("utf-8"))
            response_value = response.getvalue().decode("utf-8")
            self.assertEqual(re.sub("[а-яА-Я]+", lambda m: m.group(0)[::-1],
                             response_value), response_value)

        settings.REVERSE_RUSSIAN_WORDS = False
        for test in tests:
            for i in range(10):
                response = request.session.get(test)
            response_value = response.getvalue().decode("utf-8")
            self.assertNotEqual(re.sub("[а-яА-Я]+", lambda m: m.group(0)[::-1],
                                response_value), response_value)


    