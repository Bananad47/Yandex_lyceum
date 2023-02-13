from django.conf import settings
import re


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.cnt = 0
        self.state = settings.REVERSE_RUSSIAN_WORDS

    def __call__(self, request):
        response = self.get_response(request)
        self.cnt += 1
        if self.state and self.cnt >= 10:
            self.cnt = 0
            response_text = response.getvalue().decode("utf-8")
            reversed_text = re.sub(
                "[а-яА-Я]+", lambda m: m.group(0)[::-1], response_text
            )
            response.content = reversed_text

        return response
