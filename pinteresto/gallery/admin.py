from django.contrib import admin
from .models import Comment, Post, View

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(View)