from django.urls import path
from .views import *

urlpatterns = [
    path('post/', post),
    path('author/', author)
]