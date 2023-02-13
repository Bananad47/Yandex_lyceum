from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_item_list_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint(self):
        good_tests_list = [
            "/catalog/55/",
            "/catalog/12354/",
            "/catalog/1/",
            "/catalog/777/",
        ]

        bad_tests_list = [
            "/catalog/-1/",
            "/catalog/-23/",
            "/catalog/asdf/",
            "/catalog/i123/",
            "/catalog/123/123/",
            "/catalog/123/asdf/",
            "/catalog/asdf/123/",
        ]

        for request in good_tests_list:
            response = Client().get(request)
            self.assertEqual(response.status_code, 200)

        for request in bad_tests_list:
            response = Client().get(request)
            self.assertNotEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, 418)
        self.assertEqual(
            response.getvalue().decode("utf-8"), "<body>Я чайник</body>"
        )

    def test_regular_page(self):
        good_tests_list = [
            "/catalog/re/122234/hello/",
            "/catalog/re/12311114/hello/about/",
            "/catalog/re/134/1234/",
            "/catalog/re/123/",
            "/catalog/re/5/",
        ]

        bad_tests_list = [
            "/catalog/re/abc/abc/",
            "/catalog/re/i1234/",
            "/catalog/re/1234c/ddd/ddd",
            "/catalog/re/0/",
        ]

        for request in good_tests_list:
            response = Client().get(request)
            self.assertEqual(response.status_code, 200)

        for request in bad_tests_list:
            response = Client().get(request)
            self.assertNotEqual(response.status_code, 200)

    def test_convector(self):
        good_tests_list = [
            "/catalog/convector/122234/",
            "/catalog/convector/12/",
            "/catalog/convector/1123/",
            "/catalog/convector/1/",
        ]

        bad_tests_list = [
            "/catalog/convector/-1/",
            "/catalog/convector/12.34/",
            "/catalog/convector/abc",
        ]

        for request in good_tests_list:
            response = Client().get(request)
            self.assertEqual(response.status_code, 200)

        for request in bad_tests_list:
            response = Client().get(request)
            self.assertNotEqual(response.status_code, 200)
