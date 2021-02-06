from PIL import Image

from src.storage import get_image


# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
def scale_image(img, target_value, orientation="horizontal"):
    """Scales an image based on the given parameters

    :param img: Base image
    :type img: PIL image
    :param target_value: desired width or height (depending on the orientation)
    :type target_value: int
    :param orientation: Orientation of the varimage: horizontal or vertical (optional)
    :type orientation: str

    :returns: Scaled version of the input image
    :rtype: PIL image
    """
    target_value = int(target_value)
    if orientation == "horizontal":
        hpercent = (target_value / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, target_value), Image.ANTIALIAS)
    else:
        wpercent = (target_value / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((target_value, hsize), Image.ANTIALIAS)
    return img


class Varimage:
    """The Varmage class contains all functions to add more complex images to a base image.
    The main difference between this and the normal Image class is, that a Varimage can have
    a horizontal or vertical orientation, is scalable to fit a defined height/width and can
    be moved in an area by a parameter.
    You can use this class to create for example to create progress bars
    """

    def __init__(self, extra):
        """ Constructs a Varimage object.

        :param extra: Varimage configuration json
        :type extra: JSON
        """
        self.offset = tuple(extra['position_bar'])
        self.filename_bar = extra['filename_bar']
        self.height = extra['height']
        self.width = extra['width']
        self.max_v = extra['max']

    def add_varimage(self, img, progress_parameter_value, orientation="horizontal"):
        """Adds the varimage to a PIL image.

        :param img: Base image
        :type img: PIL image
        :param progress_parameter_value: Current value of the progress bar
        :type progress_parameter_value: int
        :param orientation: Orientation of the varimage: horizontal or vertical (optional)
        :type orientation: str

        :returns: The image from the parameter with the newly added varimage
        :rtype: PIL image
        """
        bar = get_image(self.filename_bar)
        if orientation == "horizontal":
            # Scale pointer to fit varimage box (width + height) while keeping the aspect ratio
            bar = scale_image(bar, self.height)

            # Move position of pointer
            offset = list(self.offset)
            ratio = self.width / self.max_v
            value = min(progress_parameter_value, self.max_v)
            progress_value = float(value) * ratio
            offset[0] += int(progress_value)
            offset = tuple(offset)

        else:
            bar = scale_image(bar, self.width, orientation)
            # Move position of pointer
            offset = list(self.offset)
            ratio = self.height / self.max_v
            value = min(progress_parameter_value, self.max_v)
            progress_value = self.max_v - float(value) * ratio
            offset[1] += int(progress_value)
            offset = tuple(offset)

        # Add pointer to base image
        img.paste(bar, offset, bar)
        return img
