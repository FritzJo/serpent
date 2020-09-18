from src.storage import get_image


class Image:
    def __init__(self, extra):
        self.image_file = extra['filename']
        self.offset = tuple(extra['offset'])

    def add_image(self, img):
        bar = get_image(self.image_file)
        img.paste(bar, self.offset)
        return img
