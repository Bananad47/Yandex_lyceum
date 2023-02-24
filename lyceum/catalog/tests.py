from django.core.exceptions import ValidationError
from django.test import Client, TestCase

from catalog import models


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
            "/catalog/8.24/",
            "/catalog/-8.24/",
        ]

        for request in good_tests_list:
            response = Client().get(request)
            self.assertEqual(response.status_code, 200)

        for request in bad_tests_list:
            response = Client().get(request)
            self.assertNotEqual(response.status_code, 200)

    def test_regular_page(self):
        good_tests_list = [
            "/catalog/re/122234/",
            "/catalog/re/12311114/",
            "/catalog/re/134/",
            "/catalog/re/1/",
            "/catalog/re/8/",
            "/catalog/re/5555555555/",
        ]

        bad_tests_list = [
            "/catalog/re/1.25/",
            "/catalog/re/abc/abc/",
            "/catalog/re/i1234/",
            "/catalog/re/1234c/ddd/ddd",
            "/catalog/re/0/",
            "/catalog/re/-23/",
            "/catalog/re/5-3/",
            "/catalog/re/-0/",
            "/catalog/re/122234/ddd/ddd",
            "/catalog/re/122234/1235/",
            "/catalog/re/0+1/",
            "/catalog/re/-8.24/",
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
            "/catalog/convector/abc/",
            "/catalog/convector/0/",
            "/catalog/convector/-17/",
            "/catalog/convector/0-1/",
            "/catalog/convector/fd/17/",
            "/catalog/convector/17/17/",
            "/catalog/convector/-8.24/",
        ]

        for request in good_tests_list:
            response = Client().get(request)
            self.assertEqual(response.status_code, 200)

        for request in bad_tests_list:
            response = Client().get(request)
            self.assertNotEqual(response.status_code, 200)


class ModelsTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.category = models.Category.objects.create(
            is_published=True,
            name="Тестовая категория",
            slug="test-category-slug",
            weight=100,
        )
        cls.tag = models.Tag.objects.create(
            is_published=True,
            name="Тестовый Тег",
            slug="test-tag-slug",
        )

    def test_unnable_create_one_letter(self):
        item_count = models.Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = models.Item(
                name="Тестовый товар",
                category=self.category,
                text="1",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTests.tag)

        self.assertEqual(models.Item.objects.count(), item_count)

    def test_create(self):
        item_count = models.Item.objects.count()
        self.item = models.Item(
            name="Тестовый товар",
            category=self.category,
            text="Превосходно и роскошно",
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelsTests.tag)

        self.assertEqual(models.Item.objects.count(), item_count + 1)
