from flask import Flask, request, send_file
import io
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

app = Flask(__name__)


@app.route('/gopher.png')
def test():
    image_text = request.args.get('text')
    img = Image.open('static/gopher.png')

    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default().font
    # Pos, text, color, font
    draw.text((0, 0), image_text, (0, 0, 0), font=font)

    output = io.BytesIO()
    img.convert('RGBA').save(output, format='PNG')
    output.seek(0, 0)

    return send_file(output, mimetype='image/png', as_attachment=False)


app.run(host="0.0.0.0", port=5000)
