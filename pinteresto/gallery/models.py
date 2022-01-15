from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    author_post = models.CharField(max_length=70)
    title = models.CharField(max_length=70)
    text = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=50)


class View(models.Model):
    view = models.ForeignKey(Post, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    pub_date_comment = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=70)



