import mimetypes
import os
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from bs4 import BeautifulSoup


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(), label="Text Editor")
    class Meta:
        model = Post
        fields = ('body',)

def home(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            task = form.cleaned_data['body']
            gfg = BeautifulSoup(task)
            Asss = gfg.get_text()
            file1 = open("NEWTEXTFILE.txt", "a")
            file1.write(Asss)
            file1.close()
    else:
        form = PostForm()
    return render(request, 'text.html', {'form': PostForm()})

def download(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'NEWTEXTFILE.txt'
    filepath = BASE_DIR + '/' + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response