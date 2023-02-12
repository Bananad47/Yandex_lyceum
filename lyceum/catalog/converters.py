class SixDigitProductIdConvecter:
    regex = "[0-9]+"

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
