import os
from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/opt/navidrome/music'
ALLOWED_EXTENSIONS = {'flac', 'mp3', 'wav'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # File saved successfully, return a success message
            return f'''
            <h1>File {filename} uploaded successfully</h1>
            <a href="{request.url}"><button>Upload another file</button></a>
            ''', 200
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <button onclick="window.location.href='/outpost.goauthentik.io/sign_out'">Logout</button>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(host='192.168.2.24', port=5001, debug=False)
