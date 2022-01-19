from django.conf import settings
from django.db import models


class Post(models.Model):

    title = models.CharField('Название', max_length=50)
    content = models.TextField("Описание", blank=True)
    tag = models.CharField("Теги", max_length=100)
    pub_date_post = models.DateTimeField("Дата публикации", auto_now_add=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    author = models.CharField("Автор", max_length=50)

    def __str__(self):
        return f"{self.title}"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-pub_date_post']


class View(models.Model):
    view = models.ForeignKey(Post, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Лайки'
        verbose_name_plural = 'Лайки'


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField("Автор", max_length=50)
    comment_text = models.CharField("Комментарий", max_length=200)
    pub_date_comment = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return f"{self.author_name}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date_comment']
