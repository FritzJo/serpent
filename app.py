import io
import os.path
from flask import Flask, request, send_file
from PIL import ImageFont
from PIL import ImageDraw

from image import scale_image
from storage import get_config, get_image, get_font

app = Flask(__name__)


@app.route('/<image_name>.png')
def test(image_name):
    layout_name = request.args.get('layout')
    stage = os.getenv('STAGE', 'dev')
    if stage == 'dev':
        if layout_name is None or not os.path.isfile('static/layouts/' + layout_name + '.json'):
            if os.path.isfile('static/layouts/' + image_name + '.json'):
                layout_name = image_name
            else:
                return "Please specify a valid layout!"
        if not os.path.isfile('static/images/' + image_name + '.png'):
            return "404 - Image not found"
    config = get_config(layout_name)

    img = get_image(image_name + '.png')
    draw = ImageDraw.Draw(img)

    for info in config['textfields']:
        color = tuple(info['color'])
        position = tuple(info['position'])
        text = request.args.get(info['name'])
        font_info = tuple(info['font'])
        try:
            font = get_font(font_info[0], font_info[1])
        except:
            font = ImageFont.load_default().font
        draw.text(position, text, color, font=font)

    output = io.BytesIO()

    for extra in config['extras']:
        if extra['type'] == "image":
            offset = tuple(extra['offset'])
            image_file = extra['filename']
            bar = get_image(image_file)
            img.paste(bar, offset)

        if extra['type'] == "varimage":
            offset = tuple(extra['position_bar'])
            filename_bar = extra['filename_bar']
            height = extra['height']
            width = extra['width']
            max_v = extra['max']

            # Load and scale pointer to fit varimage box (width + height) while keeping the aspect ratio
            bar = get_image(filename_bar)
            bar = scale_image(bar, height)

            # Move position of pointer
            offset = list(offset)
            ratio = width / max_v
            progress_value = float(request.args.get(extra['value_parameter_name'])) * ratio
            offset[0] += int(progress_value)
            offset = tuple(offset)

            # Add pointer to base image
            img.paste(bar, offset, bar)
    img.convert('RGBA').save(output, format='PNG')
    output.seek(0, 0)

    return send_file(output, mimetype='image/png', as_attachment=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
