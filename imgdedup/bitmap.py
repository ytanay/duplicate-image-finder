import math

from imgdedup import color
from imgdedup.color import Color


class Bitmap(object):

    def __init__(self, bitmap):
        self.bitmap = bitmap
        self.width = len(bitmap[0])
        self.height = len(bitmap)

    def __iter__(self):
        for y, row in enumerate(self.bitmap):
            for x, pixel in enumerate(row):
                yield x, y, pixel
