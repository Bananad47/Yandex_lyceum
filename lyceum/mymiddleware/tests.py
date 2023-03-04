from django.conf import settings
from django.test import Client, TestCase


class ReverseMiddlewareTests(TestCase):
    def test_middleware(self):
        state = settings.REVERSE_RUSSIAN_WORDS

        settings.REVERSE_RUSSIAN_WORDS = True
        client = Client()

        tests = [
            "/ru/coffee/",
            "/ru/about/",
            "/ru/catalog/15/",
            "/ru/catalog/",
        ]
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
            self.assertNotEqual(response, response_without_middleware)

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
