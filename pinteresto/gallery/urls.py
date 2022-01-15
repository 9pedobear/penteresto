from django.urls import path
from .views import *


app_name = 'news'
urlpatterns = [
    path('', index),
    path('post/<int:news_id>', news, name='detail'),
]

