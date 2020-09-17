import os

from src.storage import get_config


class Layout:

    def __init__(self, name):
        self.stage = os.getenv('STAGE', 'dev')
        self.layout_name = name

        # TODO Currently unchecked for exceptions!
        self.config = get_config(self.layout_name)

    def is_valid(self, image_name=""):
        if self.stage == 'dev':
            if self.layout_name is None or not os.path.isfile('static/layouts/' + self.layout_name + '.json'):
                if os.path.isfile('static/layouts/' + image_name + '.json'):
                    self.layout_name = image_name
                    return True
                else:
                    return False
            else:
                return True

    def get_textfields(self):
        return self.config['textfields']

    def get_extras(self):
        return self.config['extras']
