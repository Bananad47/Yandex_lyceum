from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_item_list_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_item_detail_endpoint(self):
        response = Client().get("/catalog/55")
        self.assertEqual(response.status_code, 200)
