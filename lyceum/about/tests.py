from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get("/ru/about/")
        self.assertEqual(response.status_code, 200)
