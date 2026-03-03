#!/usr/bin/env bash
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
out="${here}/out"

mkdir -p "${out}"

render() {
  local in_html="$1"
  local out_pdf="$2"

  wkhtmltopdf \
    --quiet \
    --enable-local-file-access \
    "${in_html}" \
    "${out_pdf}"
}

render "${here}/cover-a-terminal.html"    "${out}/cover-a-terminal.pdf"
render "${here}/cover-b-fracture-map.html" "${out}/cover-b-fracture-map.pdf"
render "${here}/cover-c-mosaic-graph.html" "${out}/cover-c-mosaic-graph.pdf"

echo "Rendered PDFs to: ${out}"

