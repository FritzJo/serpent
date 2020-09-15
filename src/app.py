import io
import os.path

from flask import Flask, request, send_file
from PIL import ImageDraw

from src.modules.image import add_image
from src.modules.textfield import add_textfield
from src.modules.varimage import add_varimage
from src.storage import get_config, get_image

app = Flask(__name__)

# Make sure that the working directory matches the location of app.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))


@app.route('/<image_name>.png')
def process_image(image_name):
    print(os.path.abspath(os.curdir))
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
    try:
        config = get_config(layout_name)
    except TypeError:
        return "404 - Configuration/Layout not found!"
    img = get_image(image_name + '.png')

    draw = ImageDraw.Draw(img)

    for info in config['textfields']:
        color = tuple(info['color'])
        position = tuple(info['position'])
        text = request.args.get(info['name'])
        font_info = tuple(info['font'])
        draw = add_textfield(draw, text, position, font_info, color)

    output = io.BytesIO()

    for extra in config['extras']:
        if extra['type'] == "image":
            offset = tuple(extra['offset'])
            image_file = extra['filename']
            img = add_image(img, image_file, offset)
        if extra['type'] == "varimage":
            offset = tuple(extra['position_bar'])
            filename_bar = extra['filename_bar']
            height = extra['height']
            width = extra['width']
            max_v = extra['max']
            progress_parameter_value = request.args.get(extra['value_parameter_name'])
            try:
                orientation = extra['orientation']
            except:
                # default to horizontal to retain backwards compatibility
                orientation = "horizontal"
            img = add_varimage(img, filename_bar, offset, height, width, max_v, progress_parameter_value, orientation)
    img.convert('RGBA').save(output, format='PNG')
    output.seek(0, 0)

    return send_file(output, mimetype='image/png', as_attachment=False)


@app.route('/')
def home():
    return '<h1>SerPEnT - SERverless Picture ENrichment Toolkit made for Google Cloud Run</h1>' \
           '<h2>Check out the source code at <a href="https://github.com/FritzJo/serpent">Github</a></h2>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
