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


def test_api_upload_mp3_file(base_url, upload_folder):
    files = {'file': ('test.mp3', io.BytesIO(b'fake mp3 content'))}
    expected_filename = os.path.join(upload_folder, secure_filename('test.mp3'))
    response = requests.post(f'{base_url}/', files=files)
    assert response.status_code == 200
    assert "uploaded successfully" in response.json().get("message", "")
    assert os.path.exists(expected_filename)

    if os.path.exists(expected_filename):
        os.remove(expected_filename)


def test_api_upload_flac_file(base_url, upload_folder):
    files = {'file': ('test.flac', io.BytesIO(b'fake flac content'))}
    expected_filename = os.path.join(upload_folder, secure_filename('test.flac'))
    response = requests.post(f'{base_url}/', files=files)
    assert response.status_code == 200
    assert "uploaded successfully" in response.json().get("message", "")
    assert os.path.exists(expected_filename)

    if os.path.exists(expected_filename):
        os.remove(expected_filename)


def test_api_upload_wav_file(base_url, upload_folder):
    files = {'file': ('test.wav', io.BytesIO(b'fake wav content'))}
    expected_filename = os.path.join(upload_folder, secure_filename('test.wav'))
    response = requests.post(f'{base_url}/', files=files)
    assert response.status_code == 200
    assert "uploaded successfully" in response.json().get("message", "")
    assert os.path.exists(expected_filename)

    if os.path.exists(expected_filename):
        os.remove(expected_filename)


def test_api_upload_multiple_files(base_url, upload_folder):
    files = [
        ('file[0]', ('multi1.mp3', io.BytesIO(b'fake multi mp3 content'))),
        ('file[1]', ('multi2.wav', io.BytesIO(b'fake multi wav content'))),
    ]
    expected_file1 = os.path.join(upload_folder, secure_filename('multi1.mp3'))
    expected_file2 = os.path.join(upload_folder, secure_filename('multi2.wav'))
    response = requests.post(f'{base_url}/', files=files)
    assert response.status_code == 200
    assert "2 file(s) uploaded successfully" in response.json().get("message", "")
    assert os.path.exists(expected_file1)
    assert os.path.exists(expected_file2)

    if os.path.exists(expected_file1):
        os.remove(expected_file1)
    if os.path.exists(expected_file2):
        os.remove(expected_file2)


def test_api_upload_m4a_file(base_url, upload_folder):
    files = {'file': ('test.m4a', io.BytesIO(b'fake m4a content'))}
    expected_filename = os.path.join(upload_folder, secure_filename('test.m4a'))
    response = requests.post(f'{base_url}/', files=files)
    assert response.status_code == 400
    assert "not allowed" in response.json().get("error", "")
    assert not os.path.exists(expected_filename)

    if os.path.exists(expected_filename):
        os.remove(expected_filename)
