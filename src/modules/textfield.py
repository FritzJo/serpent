from src.storage import get_font


def add_textfield(draw, text, position, font_info, color):
    font = get_font(font_info[0], font_info[1])
    draw.text(position, text, color, font=font)
    return draw
