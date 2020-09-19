from src.storage import get_image


class Image:
    """The Image class contains all functions to add additional images to a base image."""

    def __init__(self, extra):
        self.image_file = extra['filename']
        self.offset = tuple(extra['offset'])

    def add_image(self, img):
        """Adds the image defined in the extra data to a PIL image.

        :param img: Base image
        :type img: PIL image

        :returns: The image from the parameter with the newly added image
        :rtype: PIL image"""
        bar = get_image(self.image_file)
        img.paste(bar, self.offset)
        return img
