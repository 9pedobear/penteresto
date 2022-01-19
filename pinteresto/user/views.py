from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from gallery.models import Post


@login_required()
def author(request):
    posts = Post.objects.get()
    return render(request, 'user/author.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, аккаунт успешно зарегестрирован!')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})
