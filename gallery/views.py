import os

from django.shortcuts import render

from pinteresto import settings
from .models import *
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.db.models import F
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404


# Create your views here.
def home(request):
    context = {'file':FilesAdmin.objects.all()}
    return render(request, 'gallery/home.html', context=context)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(),
                                    content_type='application/adminupload')
            response['Content-Disposition'] = \
                'inline;filname='+os.path.basename(file_path)
            return response
    raise Http404


class DeleteNews(DeleteView):
    model = Blog
    success_url = reverse_lazy('detail')

class UpdateNews(UpdateView):
    model = Blog
    fields = ['title', 'text', 'category', 'image']
    template_name_suffix = '_update_form'

class CreateNews(CreateView):
    form_class = NewsForm
    # model = Blog
    # fields = ['title', 'text', 'category', 'image', 'author', 'is_published',
    #           'slug']
    template_name = 'gallery/add_post.html'


class Index(ListView):
    model = Blog
    context_object_name = 'posts'
    template_name = 'gallery/index.html'


class PostView(DetailView):
    model = Blog
    context_object_name = 'postview'
    template_name = 'gallery/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context