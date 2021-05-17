from django import forms
from ckeditor.widgets import CKEditorWidget
from django.shortcuts import render
from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(), label="Text Editor")
    class Meta:
        model = Post
        fields = ('body',)

def home(request):
    form = PostForm()
    return render(request, 'text.html', {'form': form})




