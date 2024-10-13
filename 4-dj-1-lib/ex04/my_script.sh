#!/bin/bash

# Create a virtual environment named django_venv using Python 3
python3 -m venv django_venv


source django_venv/bin/activate

# Install the requirements from requirements.txt
pip install --upgrade pip
pip install -r requirements.txt

echo "source django_venv/bin/activate"
# django-admin startproject myproject
# cd myproject 
# python manage.py startapp hello
# myproject/settings.py -> INSTALLED_APPS = [..., 'hello',]
# hello/views.py -> add def hello_world(request):
# myproject/urls.py -> import views + set up URL
# python manage.py migrate
# python manage.py runserver