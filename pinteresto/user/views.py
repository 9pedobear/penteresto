from django.shortcuts import render


# Create your views here.

def post(request):
    return render(request, 'user/post.html')


def author(request):
    return render(request, 'user/author.html')
