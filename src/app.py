import io
import os.path
import traceback

from flask import Flask, request, send_file

from src.image import add_extras, add_text
from src.layout import Layout
from src.storage import get_image

app = Flask(__name__)

# Make sure that the working directory matches the location of app.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))


@app.route('/<image_name>.png')
def process_image(image_name):
    """Central function of the application.

    This processes any request for an image, applies extras and manages URL parameters.

    :param image_name: Requested image
    :type image_name: str

    :returns: Final processed image with all extras
    :rtype: http response (image)
    """
    layout_name = request.args.get('layout')
    layout_object = Layout(layout_name)
    stage = os.getenv('STAGE', 'dev')
    if stage == 'dev':
        if not layout_object.is_valid(image_name):
            return "Please specify a valid layout!"
        if not os.path.isfile('static/images/' + image_name + '.png'):
            return "404 - Image not found"
    # TODO Check if file exists on gcp
    # else:

    output = io.BytesIO()
    try:
        img = get_image(image_name + '.png')
        img = add_text(img, layout_object, request)
        img = add_extras(img, layout_object, request)
    except TypeError:
        traceback.print_exc()
        img = get_image('error.png')

    img.convert('RGBA').save(output, format='PNG')
    output.seek(0, 0)
    return send_file(output, mimetype='image/png', as_attachment=False)


@app.route('/')
def home():
    """Shows a home/welcome page if the applications root directory is requested.

    :returns: Simple message with general information about the application
    :rtype: http response (html)
    """
    return '<h1>SerPEnT - SERverless Picture ENrichment Toolkit made for Google Cloud Run</h1>' \
           '<h2>Check out the source code at <a href="https://github.com/FritzJo/serpent">Github</a></h2>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
