from src.utils.storage import get_font


class Textfield:

    """The Textfield class contains all functions to add text to a base image. It handles parameters,
    like font, font size and position.
    """

    def __init__(self, info):
        """ Constructs a Textfield object.

        :param extra: Textfield configuration json
        :type extra: JSON
        """
        self.color = tuple(info['color'])
        self.position = tuple(info['position'])
        self.font_info = tuple(info['font'])

    def add_textfield(self, draw, text):
        """Adds the text defined in the textfield to a PIL image.

        :param draw: Base image
        :type draw: PIL image
        :param text: Content of the textfield
        :type text: str

        :returns: The image from the parameter with the newly added text
        :rtype: PIL image
        """
        font = get_font(self.font_info[0], self.font_info[1])
        draw.text(self.position, text, self.color, font=font)
        return draw
