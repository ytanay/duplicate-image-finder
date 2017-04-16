from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
class Color(object):

    def __init__(self, red, green, blue):
        self.red, self.green, self.blue = red, green, blue

    def __str__(self):
        return 'Color(red={}, green={}, blue={})'.format(self.red, self.green, self.blue)

    def __iter__(self):
        return iter((self.red, self.green, self.blue))

    def hex(self):
        return "#%02x%02x%02x" % (self.red, self.green, self.blue)


RED = Color(red=255, green=0, blue=0)
GREEN = Color(red=0, green=255, blue=0)
BLUE = Color(red=0, green=0, blue=255)
WHITE = Color(red=255, green=255, blue=255)
BLACK = Color(red=0, green=0, blue=0)
