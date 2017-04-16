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

    def rotate(self, angle):
        angle = math.radians(-angle)
        output = [[color.WHITE] * self.width for _ in range(self.height)]
        s, c, hw, hh = math.sin(angle), math.cos(angle), self.width//2, self.height//2
        for y in range(self.height):
            for x in range(self.width):
                x1 = x - hw
                y1 = y - hh
                output[y][x] = self.get(int(x1 * c + y1 * s + hw), int(-x1 * s + y1 * c + hh), color.WHITE)
        return Bitmap(output)

    def blur(self, iterations):
        output = self.copy()
        for _ in range(iterations):
            for y in range(output.height):
                output.bitmap[y] = ([output.average(x, y) for x in range(output.width)])
        return output

    def get(self, x, y, default=None):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.bitmap[y][x]

        return default
