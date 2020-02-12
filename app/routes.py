from flask import render_template, Flask, flash, request, redirect, url_for

from flask import send_from_directory
from app import app

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


@app.route('/')
def main():
    return("Welcome!")

@app.route('/upload', methods = ['GET','POST'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('upload.html', title = "Home")

    #r = request
    #nparr = np.formstring (r.data, np.unit8)
    #img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # do some fancy processing here....

    # build a response dict to send back to client
    #response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
    # encode response using jsonpickle
    #response_pickled = jsonpickle.encode(response)

    #return Response(response=response_pickled, status=200, mimetype="application/json")



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
