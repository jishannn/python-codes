from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import io

app = Flask(__name__)

# Allowed image formats
allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}

# function to check allowed file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check the file is part of the request
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
        
        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error='No selected file')
        
        if file and allowed_file(file.filename):
            # open the image
            img = Image.open(file)
            target_format = request.form.get('format')

            # get the format to convert to
            if target_format.lower() == 'jpg':
                target_format = 'jpeg'
            # target_format = request.form.get('format')

            # Convert RGBA to RGB when saving as JPEG (JPEG does not support transparency)
            if target_format.lower() in ["jpg", "jpeg"] and img.mode == "RGBA":
                img = img.convert("RGB")

            # convert the image to the chosen format
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format=target_format.upper())
            img_byte_arr.seek(0)

            return send_file(img_byte_arr, mimetype=f'image/{target_format.lower()}', as_attachment=True, download_name=f'converted.{target_format.lower()}')
        
        return render_template('index.html', error='Invalid file format')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)