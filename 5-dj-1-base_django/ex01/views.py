from django.shortcuts import render

def ex01(request):
    return render(request, 'ex01/base.html', {'title': 'Ex01: nav bar.'})

def django_intro(request):
    return render(request, 'ex01/django_intro.html', {'title': 'Ex01: Django, framework web.'})

def display_process(request):
    return render(request, 'ex01/display_process.html', {'title': 'Ex01: Display process of static page.'})

def template_engine(request):
    return render(request, 'ex01/template_engine.html', {'title': 'Ex01: Template Engine'})
