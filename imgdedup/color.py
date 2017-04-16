from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])


RED = Color(red=255, green=0, blue=0)
GREEN = Color(red=0, green=255, blue=0)
BLUE = Color(red=0, green=0, blue=255)
WHITE = Color(red=255, green=255, blue=255)
BLACK = Color(red=0, green=0, blue=0)
