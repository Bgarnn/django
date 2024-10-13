from django.shortcuts import render
from django.http import HttpResponse

def markdown_chetsheet(request):
    return render(request, 'ex00/index.html')
