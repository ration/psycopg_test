#!/bin/bash
PYTHON_VERSION=3.13.0
uv python install $PYTHON_VERSION
uv venv -p $PYTHON_VERSION
source .venv/bin/activate
uv pip install -r requirements.txt
python test.py
