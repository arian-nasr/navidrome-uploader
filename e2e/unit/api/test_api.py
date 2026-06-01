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

def test_api_upload_m4a_file(base_url, upload_folder):
    files = {'file': ('test.m4a', io.BytesIO(b'fake m4a content'))}
    expected_filename = os.path.join(upload_folder, secure_filename('test.m4a'))
    response = requests.post(f'{base_url}/', files=files)
    assert response.status_code == 400
    assert "not allowed" in response.json().get("error", "")
    assert not os.path.exists(expected_filename)

    if os.path.exists(expected_filename):
        os.remove(expected_filename)