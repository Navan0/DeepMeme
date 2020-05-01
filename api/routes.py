from flask import request,render_template,send_file,flash,url_for,redirect
import json
import requests
import os
from api import app
from werkzeug import secure_filename
from api.head_detecction import detect_head

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = b'fasd'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        file = request.files['photo']
        text = request.form.get("totext")
        image = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], image))
    detected = detect_head('uploads/'+str(image),text)

    if detected == 'Multiple faces in the image':
        flash('Multiple faces detected, upload single face pictures')
        return redirect(url_for('index'))

    else:
        return send_file('kids_detected.jpg', mimetype='image/jpg')



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
