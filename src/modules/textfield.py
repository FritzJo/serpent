from src.storage import get_font


class Textfield:
    def __init__(self, info):
        self.color = tuple(info['color'])
        self.position = tuple(info['position'])
        self.font_info = tuple(info['font'])

    def add_textfield(self, draw, text):
        font = get_font(self.font_info[0], self.font_info[1])
        draw.text(self.position, text, self.color, font=font)
        return draw
