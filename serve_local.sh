#!/usr/bin/env bash
set -euo pipefail

HOST="127.0.0.1"
PORT="8000"

if [[ "${1:-}" != "" ]]; then
  PORT="$1"
fi

echo "Iniciando servidor local em http://${HOST}:${PORT}/index.html"
echo "Para parar: Ctrl + C"
python3 -m http.server "$PORT" --bind "$HOST"
