from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm



def index(request):
    posts_list = Post.objects.all()
    return render(request, 'gallery/index.html', {'posts_list': posts_list})


def detail(request, pk):
    posts_list = Post.objects.all()
    try:
        post = Post.objects.get(pk=pk)
    except:
        raise Http404("Пост не найден.")

    return render(request, 'gallery/post.html', {'post': post, 'posts_list': posts_list})


@login_required()
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            print('post_new')
            return redirect('/', pk=post.pk)
    else:
        form = PostForm()
        print('post_else')
    return render(request, 'gallery/post_edit.html', {'form': form})


@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'gallery/post_edit.html', {'form': form})
