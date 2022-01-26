from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.models import News, Comments, Category, Likes
from django.http import Http404, HttpResponse
from .forms import AddPostForm, AddCommentForm


# Create your views here.


def index(request):
    all_news = News.objects.filter()
    print(request.GET)
    return render(request, 'gallery/index.html', {'all_news': all_news})


def news(request, pk):
    if request.method == 'POST':
        form2 = AddCommentForm(request.POST)
        if form2.is_valid():
            try:
                list1 = form2.save(commit=False)
                list1.author_name = request.user
                # return HttpResponse(pk)
                list1.post = News.objects.get(pk=pk)
                # return HttpResponse(list1)
                list1.save()
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse('Error')

    else:

        form = AddCommentForm()
    form = AddCommentForm()
    try:
        all_das = News.objects.all()

        all_news = News.objects.get(id=pk)
        comments = Comments.objects.filter(post=pk)
    except:

        return render(request, 'gallery/detail.html', {'all_news': all_news, 'all_das': all_das, 'form': form})
        # raise Http404('Статья не найдена')
    return render(request, 'gallery/detail.html',
                  {'comments': comments, 'all_news': all_news, 'all_das': all_das, 'form': form})


@login_required()
def addpost_new(request):
    if request.method == 'POST':
        form2 = AddPostForm(request.POST, request.FILES)
        if form2.is_valid():
            try:
                list1 = form2.save(commit=False)

                list1.author = request.user
                list1.save()
                return redirect('/')
            except Exception as e:
                return HttpResponse(e)
        else:
            errors = [i for i in form2.errors]

            # return redirect(request.META.get('HTTP_REFERER', '/'))
            return render(request, 'create_post.html', {'form': form2, 'errors': errors})

    else:
        form2 = AddPostForm()

    context = {'form': form2}
    return render(request, 'gallery/create_post.html', context)
