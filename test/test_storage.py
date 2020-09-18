import json
import os
import unittest

from PIL import Image

from src.storage import get_config, get_image

base_directory = os.path.abspath(os.curdir)


class TestLocalLoading(unittest.TestCase):

    def test_load_config(self):
        os.chdir('../src')
        example_config = '{"textfields": [ {  "name": "text", "position": [38, 5], ' \
                         ' "color": [0, 0, 0],     "font": ["Roboto-Light", 30]  }],"extras": []}   '
        expected_config = json.loads(example_config)
        config = get_config('example')
        os.chdir(base_directory)
        self.assertEqual(config, expected_config)

    def test_load_image(self):
        os.chdir('../src')
        example_image = Image.open('static/images/example.png')
        image = get_image('example.png')
        os.chdir(base_directory)
        self.assertEqual(example_image.size, image.size)

    # TODO: Test for fonts
    # TODO: Test for non-dev environments
