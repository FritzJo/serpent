from src.image import scale_image
from src.storage import get_image


class Varimage:
    def __init__(self, extra):
        self.offset = tuple(extra['position_bar'])
        self.filename_bar = extra['filename_bar']
        self.height = extra['height']
        self.width = extra['width']
        self.max_v = extra['max']

    def add_varimage(self, img, progress_parameter_value, orientation="horizontal"):
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
