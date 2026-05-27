# Navidrome Upload Utility
# Arian Nasr
# March 6, 2026

import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.environ.get('NAVIDROME_MUSIC_FOLDER', '/opt/navidrome/music')
ALLOWED_EXTENSIONS = {'flac', 'mp3', 'wav'}
MAX_CONTENT_LENGTH = 500 * 1024 * 1024

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/ping')
def ping():
    return 'pong', 200

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_count = 0
        for key, file in request.files.items():
            if key.startswith('file') and file and allowed_file(file.filename) and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                uploaded_count += 1
            else:
                return jsonify({"error": f"File '{file.filename}' is not allowed or is empty."}), 400

        return jsonify({"message": f"{uploaded_count} file(s) uploaded successfully!"}), 200

    return render_template('index.html'), 200
