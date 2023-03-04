from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_coffee_endpoint(self):
        response = Client().get("/ru/coffee/")
        self.assertEqual(response.status_code, 418)
        self.assertEqual(
            response.getvalue().decode("utf-8"), "<body> Я чайник </body>"
        )
