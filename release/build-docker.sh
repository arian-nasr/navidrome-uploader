#!/bin/sh
set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
PROJECT_ROOT="$(CDPATH= cd -- "${SCRIPT_DIR}/.." && pwd)"

cd "${PROJECT_ROOT}"

docker build --platform linux/amd64 -t uploader-builder -f Dockerfile.build .

docker run --name uploader-builder-container --platform linux/amd64 uploader-builder

docker cp uploader-builder-container:/dist/. output/

docker rm uploader-builder-container