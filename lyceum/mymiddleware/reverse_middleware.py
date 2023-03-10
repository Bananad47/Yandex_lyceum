import re

from django.conf import settings


class ReverseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.cnt = 0
        self.state = settings.REVERSE_RUSSIAN_WORDS

    def __call__(self, request):
        response = self.get_response(request)
        self.cnt += 1
        if self.state is True and self.cnt >= 10:
            self.cnt = 0
            response_text = response.getvalue().decode("utf-8")
            reversed_text = re.sub(
                r"\b([А-Яа-яёЁ]+[^a-zA-Z<\W])\b",
                lambda m: m.group(0)[::-1],
                response_text,
            )
            response.content = reversed_text

        return response
