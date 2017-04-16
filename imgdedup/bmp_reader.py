import collections

import struct


BMPMetadata = collections.namedtuple('BMPMetadata', [field[0] for field in BMP_FIELDS])


class BMPFile(object):
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

    FORMAT_STRING = '<' + ''.join(FORMAT_CHARS[field[1]] for field in BMP_FIELDS)

