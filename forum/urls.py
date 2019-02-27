from django.urls import path
from .views import home

"""Urls for forum and main pagepp"""

app_name = 'forum'
urlpatterns = [
    path('', home, name='home')
]