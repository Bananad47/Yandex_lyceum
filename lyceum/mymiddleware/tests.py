import re

from django.conf import settings
from django.test import Client, TestCase


class ReverseMiddlewareTests(TestCase):
    def test_middleware(self):
        state = settings.REVERSE_RUSSIAN_WORDS

        settings.REVERSE_RUSSIAN_WORDS = True
        client = Client()
        tests = ["/coffee/", "/about/", "/catalog/15/", "/catalog/"]
        for test in tests:
            for i in range(9):
                response = client.get(test).content.decode("utf-8")
                response_without_middleware = (
                    Client().get(test).content.decode("utf-8")
                )

                self.assertEqual(response, response_without_middleware)

            response = client.get(test).content.decode("utf-8")
            reversed_response = re.sub(
                r"\s[а-яА-Я]+\s", lambda m: m.group(0)[::-1], response
            )
            response_without_middleware = (
                Client().get(test).content.decode("utf-8")
            )
            self.assertEqual(reversed_response, response_without_middleware)

        settings.REVERSE_RUSSIAN_WORDS = False
        client = Client()

        for test in tests:
            for i in range(9):
                response = client.get(test).content.decode("utf-8")
                response_without_middleware = (
                    Client().get(test).content.decode("utf-8")
                )

                self.assertEqual(response, response_without_middleware)

            response = client.get(test).content.decode("utf-8")
            response_without_middleware = (
                Client().get(test).content.decode("utf-8")
            )
            self.assertEqual(response, response_without_middleware)

        settings.REVERSE_RUSSIAN_WORDS = state
