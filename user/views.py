from django.shortcuts import render, redirect
from gallery.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {"form": form})


def login(request):
    return render(request, 'user/login.html')



def author(request):
    posts = Blog.objects.all()
    return render(request, 'user/author.html', {'posts':posts})


