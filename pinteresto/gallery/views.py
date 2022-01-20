from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Post
from .forms import PostForm


def index(request):
    posts_list = Post.objects.all()
    return render(request, 'gallery/index.html', {'posts_list': posts_list})


def detail(request, pk):
    posts_list = Post.objects.all()
    try:
        post = Post.objects.get(pk=pk)
        post.views.add(request.user)
        total_likes = post.total_likes()
        total_views = post.total_views()
    except:
        raise Http404("Пост не найден.")
    return render(request, 'gallery/post.html', {'post': post, 'posts_list': posts_list, 'total_likes': total_likes, 'total_views': total_views})


@login_required()
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'gallery/post_edit.html', {'form': form})


@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'gallery/post_edit.html', {'form': form})


@login_required()
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect("/")


@login_required()
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('gallery:detail', args=[str(pk)]))
