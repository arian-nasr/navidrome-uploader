#!/bin/sh

export NAVIDROME_MUSIC_FOLDER="/opt/navidrome/music"
export BASE_URL="http://127.0.0.1:5001"

# Start the app manually since systemd isn't running in the container
cd /opt/navidrome-uploader
su -s /bin/sh navidrome-uploader -c "/opt/navidrome-uploader/venv/bin/gunicorn --no-control-socket -c gunicorn.conf.py main:app" &

APP_PID=$!

TIMEOUT=30
SERVICE_UP=0

while [ $TIMEOUT -gt 0 ]; do
    if curl -s $BASE_URL/ping | grep -q "pong"; then
        SERVICE_UP=1
        break
    fi
    sleep 1
    TIMEOUT=$((TIMEOUT-1))
done

if [ $SERVICE_UP -eq 0 ]; then
    echo "Error: Service failed to start within the timeout period"
    kill $APP_PID
    exit 1
fi

cd /e2e

/e2e/venv/bin/pytest unit/api/test_api.py

# Capture the exit code of pytest
TEST_EXIT_CODE=$?

kill $APP_PID

exit $TEST_EXIT_CODE