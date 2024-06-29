"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Головна сторінка
    path('', views.index, name='index' ),
    # Сторінка що відображає всі теми
    path('topics/', views.topics, name='topics'),
]