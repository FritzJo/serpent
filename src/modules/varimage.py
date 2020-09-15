from src.image import scale_image
from src.storage import get_image


def add_varimage(img, filename_bar, offset, height, width, max_v, progress_parameter_value, orientation="horizontal"):
    bar = get_image(filename_bar)
    if orientation == "horizontal":
        # Scale pointer to fit varimage box (width + height) while keeping the aspect ratio
        bar = scale_image(bar, height)

        # Move position of pointer
        offset = list(offset)
        ratio = width / max_v
        value = min(progress_parameter_value, max_v)
        progress_value = float(value) * ratio
        offset[0] += int(progress_value)
        offset = tuple(offset)

    else:
        bar = scale_image(bar, width, orientation)
        # Move position of pointer
        offset = list(offset)
        ratio = height / max_v
        value = min(progress_parameter_value, max_v)
        progress_value = max_v - float(value) * ratio
        offset[1] += int(progress_value)
        offset = tuple(offset)

    # Add pointer to base image
    img.paste(bar, offset, bar)
    return img
