# from django.conf import settings
# from django.test import Client, TestCase


# class StaticURLTests(TestCase):
#     def test_middleware(self):
#         state = settings.REVERSE_RUSSIAN_WORDS
#         settings.REVERSE_RUSSINAN_WORDS = True
#         tests = ["/catalog/", "/coffee/", "/catalog/15/", "/about/",
# "/", "/catalog/re/1234/"]
#         client = Client()
#         for test in tests:
#             for i in range(10):
#                 response = client.get(test)
#                 print(response, response.content.decode("utf-8"))
