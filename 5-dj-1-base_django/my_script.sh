#!/bin/bash

# Create a virtual environment named django_venv using Python 3
python3 -m venv django_venv


source django_venv/bin/activate

# Install the requirements from requirements.txt
pip install --upgrade pip
pip install -r requirements.txt

# django-admin startproject 05
# cd d05
# python manage.py startapp ex00
# d05/settings.py -> INSTALLED_APPS = [..., 'ex00',]
# ex00/views.py 
# ex00/urls.py
# d05/urls.py
# create folder in -> mkdir -p ex00/templates/ex00 -> index.html
# python manage.py migrate
# @d05 -> python manage.py runserver

# @d05 -> python manage.py startapp ex01
# d05/urls.py
# ex01/urls.py
# ex01/views.py 
# create folder in -> mkdir -p ex01/templates/ex01 -> base.html,...,...html
# create folder in -> mkdir -p ex01/static/css -> style1.css, style2.css
# d05/settings.py -> INSTALLED_APPS = [..., 'ex01',]
# d05/settings.py -> STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') STATICFILES_DIRS = [os.path.join(BASE_DIR, 'ex01/static'),]
# @d05 -> python manage.py collectstatic
# @d05 -> python manage.py runserver

# source django_venv/bin/activate
# @d05 -> python manage.py startapp ex02
# d05/settings.py -> INSTALLED_APPS = [..., 'ex02',], LOG_FILE_PATH = os.path.join(BASE_DIR, 'ex02/logs.txt')
# ex02/forms.py
# ex02/views.py
# ex02/templates/ex02/index.html
# ex02/urls.py
# d05/urls.py
# @d05 -> python manage.py runserver

# source django_venv/bin/activate
# @d05 -> python manage.py startapp ex03
# d05/settings.py -> INSTALLED_APPS = [..., 'ex03',]
# ex03/views.py
# ex03/templates/ex02/index.html
# ex03/urls.py
# d05/urls.py
