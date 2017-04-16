import os

from imgdedup.bmp_reader import BMPFile, BMPMetadata

RESOURCES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')


def test_bmp_metadata_parser():
    file_path = os.path.join(RESOURCES_PATH, '2by2.bmp')
    with open(file_path, 'rb') as f:
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
