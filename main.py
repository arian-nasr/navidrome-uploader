import os
from flask import Flask, request
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
        if 'file' not in request.files:
            return 'No file part', 400
        files = request.files.getlist('file')
        for file in files:
            if file.filename == '':
                return 'No selected file', 400
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                return 'File extension not allowed', 400
        return f'''
        <!doctype html>
        <title>Upload successful</title>
        <h1>{len(files)} file(s) uploaded successfully</h1>
        <a href="{request.url}"><button>Upload another file</button></a>
        ''', 200

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <button onclick="window.location.href='/outpost.goauthentik.io/sign_out'">Logout</button>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file multiple>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(host='192.168.2.24', port=5001, debug=False)
