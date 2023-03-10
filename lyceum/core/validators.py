import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class custom_validator(object):
    def __init__(self, *words):
        self.words = words

    def __call__(self, value):
        for word in self.words:
            if re.findall(r"\b({})\b".format(word), value.lower()) == []:
                raise ValidationError(f"Ваш текст не содержит слова {word}!")
        return self
