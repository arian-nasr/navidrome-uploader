# Navidrome Upload Utility
# Arian Nasr
# March 6, 2026

import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.environ.get('NAVIDROME_MUSIC_FOLDER', '/opt/navidrome/music')
BIND_ADDRESS = os.environ.get('BIND_ADDRESS', '0.0.0.0')
BIND_PORT = int(os.environ.get('BIND_PORT', 5001))
ALLOWED_EXTENSIONS = {'flac', 'mp3', 'wav'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/ping')
def ping():
    return 'pong', 200

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for key, file in request.files.items():
            if key.startswith('file') and file and allowed_file(file.filename) and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                return render_template('error.html', error_message=f'File is not allowed.'), 400

        return render_template('success.html', success_message=f'{len(request.files)} file(s) uploaded successfully!'), 200

    return render_template('index.html'), 200


if __name__ == '__main__':
    app.run(host=BIND_ADDRESS, port=BIND_PORT, debug=False)
