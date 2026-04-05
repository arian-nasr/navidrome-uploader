#!/bin/sh

if ! getent passwd navidrome-uploader > /dev/null 2>&1; then
    printf "Creating navidrome-uploader user\n"
    useradd --system --shell /usr/sbin/nologin --user-group navidrome-uploader
fi