from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

app_name = 'gallery'
urlpatterns = [
    path('', index),
    path('post/<int:post_id>', detail, name='detail')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

