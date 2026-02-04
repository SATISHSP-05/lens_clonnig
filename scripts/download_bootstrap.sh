#!/usr/bin/env sh
set -eu

VERSION="5.3.3"
BASE_URL="https://cdn.jsdelivr.net/npm/bootstrap@${VERSION}/dist"
DEST="$(cd "$(dirname "$0")/../backend/static/vendor/bootstrap" && pwd)"

mkdir -p "$DEST"
curl -fsSL "${BASE_URL}/css/bootstrap.min.css" -o "${DEST}/bootstrap.min.css"
curl -fsSL "${BASE_URL}/js/bootstrap.bundle.min.js" -o "${DEST}/bootstrap.bundle.min.js"

echo "Downloaded Bootstrap ${VERSION} to ${DEST}"
