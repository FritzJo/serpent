from src.storage import get_image


def add_image(img, image_file, offset):
    bar = get_image(image_file)
    img.paste(bar, offset)
    return img
