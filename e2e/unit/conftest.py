import pytest
import os

@pytest.fixture(scope='session')
def base_url():
    return os.getenv('BASE_URL', 'http://127.0.0.1:5001')

@pytest.fixture(scope='session')
def upload_folder():
    return os.getenv('NAVIDROME_MUSIC_FOLDER', '/opt/navidrome/music')