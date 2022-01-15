from django.shortcuts import render
from user.models import News, Comments, Category, Likes
from django.http import Http404


# Create your views here.


def index(request):
    all_news = News.objects.all()
    return render(request, 'gallery/index.html', {'all_news': all_news})


def news(request, news_id):
    try:
        all_das = News.objects.all()
        all_news = News.objects.get(id=news_id)
        comments = Comments.objects.get(post=news_id)
    except:
        return render(request, 'gallery/detail.html', {'all_news': all_news, 'all_das': all_das})
        # raise Http404('Статья не найдена')
    return render(request, 'gallery/detail.html', {'comments': comments, 'all_news': all_news, 'all_das':all_das})
