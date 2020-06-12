import json
import io
import os.path
from flask import Flask, request, send_file
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

app = Flask(__name__)


@app.route('/<image_name>.png')
def test(image_name):
    layout_name = request.args.get('layout')
    if layout_name is None or not os.path.isfile('static/layouts/' + layout_name + '.json'):
        return "Please specify a valid layout!"
    config = load_config(layout_name)

    if not os.path.isfile('static/images/' + image_name + '.png'):
        return "404 - Image not found"
    img = Image.open('static/images/' + image_name + '.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default().font

    for info in config['textfields']:
        color = tuple(info['color'])
        position = tuple(info['position'])
        text = request.args.get(info['name'])
        draw.text(position, text, color, font=font)

    output = io.BytesIO()

    for overlays in config['extras']:
        offset = tuple(overlays['offset'])
        image_file = overlays['filename']
        bar = Image.open('static/images/' + image_file)
        img.paste(bar, offset)

    img.convert('RGBA').save(output, format='PNG')
    output.seek(0, 0)

    return send_file(output, mimetype='image/png', as_attachment=False)


def load_config(name):
    with open('static/layouts/' + name + '.json') as json_file:
        data = json.load(json_file)
        return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
