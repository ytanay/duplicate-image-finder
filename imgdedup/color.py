from collections import namedtuple

class Color(object):

    def __init__(self, red, green, blue):
        self.red, self.green, self.blue = red, green, blue

    def __str__(self):
        return 'Color(red={}, green={}, blue={})'.format(self.red, self.green, self.blue)

    def __iter__(self):
        return iter((self.red, self.green, self.blue))

    def hex(self):
        return "#%02x%02x%02x" % (self.red, self.green, self.blue)

    def greyscale(self):
        return Color(*(sum(self) // 3,) * 3)

    def difference(self, other):
        return Color(*(abs(x - y) for x, y in zip(self, other)))

    @classmethod
    def average(cls, *args):
        return cls(*(sum(vals) // len(args) for vals in zip(*args)))



RED = Color(red=255, green=0, blue=0)
GREEN = Color(red=0, green=255, blue=0)
BLUE = Color(red=0, green=0, blue=255)
WHITE = Color(red=255, green=255, blue=255)
BLACK = Color(red=0, green=0, blue=0)
