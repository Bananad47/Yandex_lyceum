class SixDigitProductIdConvecter:
    regex = "[1-9][0-9]+|[1-9]"

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
