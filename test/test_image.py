import unittest

from PIL import Image

from src.modules.varimage import scale_image


class TestScaling(unittest.TestCase):
    def test_no_scaling(self):
        img = Image.open('../src/static/images/example.png')
        _, current_height = img.size
        img_scaled = scale_image(img, current_height)
        self.assertEqual(img.size, img_scaled.size)

    def test_50_scaling(self):
        img = Image.open('../src/static/images/example.png')
        _, current_height = img.size
        img_scaled = scale_image(img, current_height / 2)
        self.assertEqual(img.size[0] / 2, img_scaled.size[0])
        self.assertEqual(img.size[1] / 2, img_scaled.size[1])

    def test_150_scaling(self):
        img = Image.open('../src/static/images/example.png')
        current_width, current_height = img.size
        img_scaled = scale_image(img, current_height * 2)
        self.assertEqual(img.size[0] * 2, img_scaled.size[0])
        self.assertEqual(img.size[1] * 2, img_scaled.size[1])

    def test_0_scaling(self):
        img = Image.open('../src/static/images/example.png')
        self.assertRaises(ValueError, scale_image, img, 0)

    def test_negative_scaling(self):
        img = Image.open('../src/static/images/example.png')
        self.assertRaises(ValueError, scale_image, img, -100)
