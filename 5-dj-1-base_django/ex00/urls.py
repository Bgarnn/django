from django.urls import path
from .views import markdown_chetsheet

urlpatterns = [
    path('', markdown_chetsheet, name='markdown_cheatsheet')
]