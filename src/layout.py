import os

from src.storage import get_config


class Layout:
    """The Layout class represents a loaded layout file. It contains functions to validate a
    layout and access its components."""

    def __init__(self, name):
        self.stage = os.getenv('STAGE', 'dev')
        self.layout_name = name

        # TODO Currently unchecked for exceptions!
        self.config = get_config(self.layout_name)

    def is_valid(self, image_name=""):
        """Check if the input is a valid layout name

        This function firstly checks, if the variable 'layout_name' actually contains something.
        If that is not the case, or no layout file with a matching name exists in the layout folder,
        the function looks for a layout with the name of the provided image name variable.

        :param image_name: name of the image file (optional)
        :type image_name: str

        :returns: If the object has a valid layout name and that layout also exists
        :rtype: bool"""
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
        """Getter for textfields

        Returns all textfields defined in the loaded layout

        :returns: a JSON array with all textfields from the layout
        :rtype: list"""
        return self.config['textfields']

    def get_extras(self):
        """Getter for extra elements

        Returns all extras defined in the loaded layout

        :returns: a JSON array with all extras from the layout
        :rtype: list"""
        return self.config['extras']
