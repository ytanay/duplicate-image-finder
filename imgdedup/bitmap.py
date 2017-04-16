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
    def copy(self):
        return Bitmap([row[:] for row in self.bitmap])
    def scale(self, ratio):
        output, width, height = [], round(self.width * ratio), round(self.height * ratio)
        for y in range(height):
            original_y = int(y // ratio)
            output.append([self.bitmap[original_y][int(x // ratio)] for x in range(width)])

        return Bitmap(output)
    def get(self, x, y, default=None):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.bitmap[y][x]

        return default
