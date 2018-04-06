from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import zipfile
from .models import Document
from .forms import DocumentForm

def home(request):
    documents = Document.objects.all()
    return render(request, '/home', { 'documents': documents })

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        file_name = request.FILES['document'].name

        ###
        #import zipfile
        #f = zipfile.ZipFile("Adolf.zip")
        #f.extractall()
        ###
        #unzipfile = zipfile(request.FILES['document']);
        #unzipfile.extractall();
        #unzipfile.close();
        ###
        #content = request.FILES['document']
        #unzipped = zipfile.ZipFile(content);
        ###

        if form.is_valid() and file_name.endswith('.zip'):
            form.save()
            return redirect('/allContent')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})






