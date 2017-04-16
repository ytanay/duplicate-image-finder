import os

import pytest

from imgdedup import color
from imgdedup.bmp_reader import BMPFile, BMPMetadata

RESOURCES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')
EX_2BY2 = os.path.join(RESOURCES_PATH, '2by2.bmp')


def test_bmp_metadata_parser():

    with open(EX_2BY2, 'rb') as f:
        bmp = BMPFile.read(f)
        assert bmp.width == bmp.height == 2
        assert bmp.metadata == BMPMetadata(
            id=19778,
            size=70,
            opt1=0,
            opt2=0,
            bitmap_offset=54,
            header_size=40,
            width=2,
            height=2,
            color_planes=1,
            bits_per_pixel=24,
            compression=0,
            bitmap_size=16,
            print_width=0,
            print_height=0,
            palette_size=0,
            important_colors=0
        )


def test_get_specific_pixels():
    with open(EX_2BY2, 'rb') as f:
        bmp = BMPFile.read(f)

        assert bmp.pixel(0, 0) == color.BLUE
        assert bmp.pixel(0, 1) == color.RED
        assert bmp.pixel(1, 0) == color.GREEN
        assert bmp.pixel(1, 1) == color.WHITE


def test_bounds_checking():
    with open(EX_2BY2, 'rb') as f:
        bmp = BMPFile.read(f)

        with pytest.raises(ValueError):
            bmp.pixel(2, 0)

        with pytest.raises(ValueError):
            bmp.pixel(-1, 0)
