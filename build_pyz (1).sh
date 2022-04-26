#!/usr/bin/env bash
set -e

rm -rfv build_pyz_output
pip install -t build_pyz_output .
python -m zipapp build_pyz_output --main "hello:main" --python "/usr/bin/env python3" --output "hello-0.1.0.pyz"
