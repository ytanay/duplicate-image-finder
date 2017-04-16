import collections

import struct

from imgdedup.bitmap import Bitmap
from imgdedup.color import Color

BMP_FIELDS = [
    ('id', 2),
    ('size', 4),
    ('opt1', 2),
    ('opt2', 2),
    ('bitmap_offset', 4),
    ('header_size', 4),
    ('width', 4),
    ('height', 4),
    ('color_planes', 2),
    ('bits_per_pixel', 2),
    ('compression', 4),
    ('bitmap_size', 4),
    ('print_width', 4),
    ('print_height', 4),
    ('palette_size', 4),
    ('important_colors', 4)
]

FORMAT_CHARS = {
    4: 'L',
    2: 'H'
}


BMPMetadata = collections.namedtuple('BMPMetadata', [field[0] for field in BMP_FIELDS])


class BMPFile(object):

    HEADER_FORMAT_STRING = '<' + ''.join(FORMAT_CHARS[field[1]] for field in BMP_FIELDS)
    PIXEL_FORMAT_STRING = '<BBB'

    def __init__(self, metadata, data):
        self.width, self.height = metadata.width, metadata.height
        self.row_offset = self.compute_row_offset(self.width)
        self.metadata = metadata
        self.data = data

    def offset(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError('Pixel not in bounds')

        return (self.height - y - 1) * self.row_offset + (x * 3)

    def pixel(self, x, y):
        return Color(*reversed(struct.unpack_from(self.PIXEL_FORMAT_STRING, self.data, self.offset(x, y))))

    def bitmap(self):
        return Bitmap([[self.pixel(x, y) for x in range(self.width)] for y in range(self.height)])

    @staticmethod
    def compute_row_offset(width):
        bytes_per_row = width * 3
        return bytes_per_row if width % 4 == 0 else ((bytes_per_row // 4) + 1) * 4

    @classmethod
    def read(cls, file_handle):
        contents = file_handle.read()
        metadata = BMPMetadata(*struct.unpack_from(cls.HEADER_FORMAT_STRING, contents))
        assert metadata.id == 0x4D42

        return cls(metadata, contents[metadata.bitmap_offset:])
