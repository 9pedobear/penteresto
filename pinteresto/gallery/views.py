from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from user.models import Post


def index(request):
    posts_list = Post.objects.all()
    return render(request, 'gallery/index.html', {'posts_list': posts_list})

def detail(request, post_id):
    try:
        a = Post.objects.get(id=post_id)
    except:
        raise Http404("Пост не найден.")

    return render(request, 'gallery/post.html', {'post': a})