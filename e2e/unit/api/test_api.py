import pytest
import requests
import io
import os
from werkzeug.utils import secure_filename


def test_api_ping(base_url):
    response = requests.get(f'{base_url}/ping')
    assert response.status_code == 200
    assert response.text == 'pong'

def test_api_upload_non_audio_file(base_url, upload_folder):
    files = {'file': ('test.txt', io.BytesIO(b'not an audio file'))}
    expected_filename = os.path.join(upload_folder, secure_filename('test.txt'))
    response = requests.post(f'{base_url}/', files=files)
    assert response.status_code == 400
    assert "not allowed" in response.json().get("error", "")
    assert not os.path.exists(expected_filename)

    if os.path.exists(expected_filename):
        os.remove(expected_filename)