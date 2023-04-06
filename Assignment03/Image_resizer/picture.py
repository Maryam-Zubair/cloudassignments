import io
from flask import Flask, request, render_template, send_file
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def resize_image():
    # Get the uploaded image and size data from the form
    img = Image.open(request.files['image'])
    width = int(request.form['width'])
    height = int(request.form['height'])

    # Resize the image using Pillow
    resized_img = img.resize((width, height))

    # Return the resized image as a downloadable file
    img_bytes = io.BytesIO()
    resized_img.save(img_bytes, format='JPEG')
    img_bytes.seek(0)

    return send_file(
        img_bytes,
        as_attachment=True,
        download_name='resized_image.jpg',
        mimetype='image/jpeg'
    )

if __name__ == '__main__':
    app.run(debug=True)