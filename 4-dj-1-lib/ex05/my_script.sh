#!/bin/bash

# Create a virtual environment named django_venv using Python 3
python3 -m venv django_venv


source django_venv/bin/activate

# Install the requirements from requirements.txt
pip install --upgrade pip
pip install -r requirements.txt

echo "source django_venv/bin/activate"
