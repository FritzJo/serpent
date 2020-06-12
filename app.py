from flask import Flask, request, send_file
import io
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

app = Flask(__name__)


@app.route('/gopher.png')
def test():
    image_text = request.args.get('text')
    img = Image.open('static/image_boxes.png')

    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default().font
    # Pos, text, color, font
    # Klasse
    draw.text((400, 555), image_text, (0, 0, 0), font=font)
    # Flugzeit
    draw.text((400, 612), image_text, (0, 0, 0), font=font)
    # Sitzplatz
    draw.text((400, 668), image_text, (0, 0, 0), font=font)
    # Ticketpreis
    draw.text((900, 584), image_text, (0, 0, 0), font=font)
    # CO2
    draw.text((900, 651), image_text, (0, 0, 0), font=font)

    output = io.BytesIO()
    img.convert('RGBA').save(output, format='PNG')
    output.seek(0, 0)

    return send_file(output, mimetype='image/png', as_attachment=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
