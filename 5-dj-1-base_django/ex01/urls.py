from django.urls import path
from . import views

urlpatterns = [
    path('', views.ex01, name='nav'),
    path('django/', views.django_intro, name='django_intro'),
    path('display/', views.display_process, name='display_process'),
    path('templates/', views.template_engine, name='template_engine'),
]