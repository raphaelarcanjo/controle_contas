from django.urls import path
from contas import views

urlpatterns = [
    path('', views.index, name='index')
]