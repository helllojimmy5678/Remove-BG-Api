from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/convert-to-png', methods=['POST'])
def convert_to_png():
    image = request.files['image'].read()
    image = Image.open(io.BytesIO(image))
    output = io.BytesIO()
    image.save(output, format='PNG')
    output.seek(0)
    return send_file(output, mimetype='image/png')

if __name__ == '__main__':
    app.run()
