from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from catalog import models


class StaticURLTests(TestCase):
    def test_item_list_endpoint(self):
        response = Client().get("/ru/")
        self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint(self):
        bad_tests_list = [
            "/ru/catalog/-1/",
            "/ru/catalog/-23/",
            "/ru/catalog/asdf/",
            "/ru/catalog/i123/",
            "/ru/catalog/123/123/",
            "/ru/catalog/123/asdf/",
            "/ru/catalog/asdf/123/",
            "/ru/catalog/8.24/",
            "/ru/catalog/-8.24/",
        ]

        for request in bad_tests_list:
            response = Client().get(request)
            self.assertNotEqual(response.status_code, 200)

    def test_regular_page(self):
        good_tests_list = [
            "/ru/catalog/re/122234/",
            "/ru/catalog/re/12311114/",
            "/ru/catalog/re/134/",
            "/ru/catalog/re/1/",
            "/ru/catalog/re/8/",
            "/ru/catalog/re/5555555555/",
        ]

        bad_tests_list = [
            "/ru/catalog/re/1.25/",
            "/ru/catalog/re/abc/abc/",
            "/ru/catalog/re/i1234/",
            "/ru/catalog/re/1234c/ddd/ddd",
            "/ru/catalog/re/0/",
            "/ru/catalog/re/-23/",
            "/ru/catalog/re/5-3/",
            "/ru/catalog/re/-0/",
            "/ru/catalog/re/122234/ddd/ddd",
            "/ru/catalog/re/122234/1235/",
            "/ru/catalog/re/0+1/",
            "/ru/catalog/re/-8.24/",
        ]

        for request in good_tests_list:
            response = Client().get(request)
            self.assertEqual(response.status_code, 200)

        for request in bad_tests_list:
            response = Client().get(request)
            self.assertNotEqual(response.status_code, 200)

    def test_convector(self):
        good_tests_list = [
            "/ru/catalog/convector/122234/",
            "/ru/catalog/convector/12/",
            "/ru/catalog/convector/1123/",
            "/ru/catalog/convector/1/",
        ]

        bad_tests_list = [
            "/ru/catalog/convector/-1/",
            "/ru/catalog/convector/12.34/",
            "/ru/catalog/convector/abc/",
            "/ru/catalog/convector/0/",
            "/ru/catalog/convector/-17/",
            "/ru/catalog/convector/0-1/",
            "/ru/catalog/convector/fd/17/",
            "/ru/catalog/convector/17/17/",
            "/ru/catalog/convector/-8.24/",
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
            name="???????????????? ??????????????????",
            slug="test-category-slug",
            weight=100,
        )

        cls.tag = models.Tag.objects.create(
            is_published=True,
            name="???????????????? ??????",
            slug="test-tag-slug",
        )

    def test_unnable_create_not_luxurious_text(self):
        item_count = models.Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = models.Item(
                name="???????????????? ??????????",
                category=self.category,
                text="??????????????????????",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTests.tag)

        self.assertEqual(models.Item.objects.count(), item_count)

    def test_unnable_create_not_great_text(self):
        item_count = models.Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = models.Item(
                name="???????????????? ??????????",
                category=self.category,
                text="????????????????",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTests.tag)

        self.assertEqual(models.Item.objects.count(), item_count)

    def test_create(self):
        item_count = models.Item.objects.count()
        self.item = models.Item(
            name="???????????????? ??????????",
            category=self.category,
            text="?????????????????????? ?? ????????????????",
            preview="\static_dev\img\icons\icon100.png",  # noqa: W605
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelsTests.tag)

        self.assertEqual(models.Item.objects.count(), item_count + 1)

    # def test_unnable_create_not_unique_tag_name(self):
    #     self.tag_count = models.Tag.objects.count()
    #     with self.assertRaises(ValidationError):
    #         self.tag2 = models.Tag.objects.create(
    #             is_published=True,
    #             name="???????????????? ??????",
    #             slug="test-tag2-slug",
    #         )
    #         self.tag2.full_clean()
    #         self.tag2.save()

    #     self.assertEqual(models.Tag.objects.count(), self.tag_count)

    # def test_unnable_create_not_unique_category_name(self):
    #     self.category_count = models.Category.objects.count()
    #     with self.assertRaises(ValidationError):
    #         self.category2 = models.Category.objects.create(
    #             is_published=True,
    #             name="???????????????? ??????????????????",
    #             slug="test-category2-slug",
    #             weight=100,
    #         )
    #         self.category2.full_clean()
    #         self.category2.save()
    #     print(
    #         [
    #             (x.name, x.slug, x.canonical_name)
    #             for x in models.Category.objects.filter()
    #         ]
    #     )
    #     self.assertEqual(models.Category.objects.count(),
    # self.category_count)


class ContextTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.category = models.Category.objects.create(
            is_published=True,
            name="???????????????? ??????????????????",
            slug="test-category-slug",
            weight=100,
        )

        cls.tag = models.Tag.objects.create(
            is_published=True,
            name="???????????????? ??????",
            slug="test-tag-slug",
        )
        cls.item = models.Item.objects.create(
            name="???????????????? ??????????",
            category=cls.category,
        )

        cls.category.clean()
        cls.category.save()
        cls.tag.clean()
        cls.tag.save()
        cls.item.clean()
        cls.item.save()
        cls.item.tags.add(cls.tag.pk)

    def test_homepage_context(self):
        response = Client().get(reverse("homepage:home"))
        self.assertIn("items", response.context)

    def test_items_list_context(self):
        response = Client().get(reverse("catalog:item_list"))
        self.assertIn("items", response.context)

    def test_item_main_page_context(self):
        response = Client().get(reverse("catalog:item_detail", args=[1]))
        self.assertIn("item", response.context)

    def test_items_list_context2(self):
        response = Client().get(reverse("catalog:item_list"))
        context = response.context["items"][0].__dict__
        category = response.context["category"][0]
        tags = (
            context["_prefetched_objects_cache"]["tags"]
            .__dict__["_result_cache"][0]
            .__dict__
        )

        self.assertNotIn("is_on_main", context)
        self.assertNotIn("is_published", context)
        self.assertNotIn("category_slug", context)
        self.assertNotIn("category_weight", context)
        self.assertNotIn("slug", tags)

        self.assertIn("name", tags)
        self.assertIn("preview", context)
        self.assertIn("text", context)
        self.assertIn("name", context)
        self.assertTrue(category)
