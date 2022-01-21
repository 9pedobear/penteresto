from django import forms
from .models import Blog


class NewsForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text', 'category', 'image', 'author',
                  'is_published', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'slug' : forms.TextInput(attrs={'class': 'form-control'})
        }