from django.shortcuts import render, redirect
from .models import Post
from core.models import Document
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
import zipfile




def index(request):

    return redirect('/allContent')

def about(request):
    return render(request, 'about.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def addNewCategory(request):
    return render(request, 'addNewCategory.html', {})

def allContent(request):
    return render(request, 'allContent.html', {})

def deleteFile(request):
    return render(request, 'deleteFile.html', {})

def search(request):
    return render(request, 'search.html', {})
def hello(request):
    return render(request, 'hello.html', {})
def list_all_posts(request):
    posts = Document.objects.all()
    context = {'posts': posts}
    return render(request, 'allContent.html', context)

def display_post(request, id):
    if request.user is None or not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    post = Document.objects.filter(pk=id)[0]

    post_url = post.document.url

    ####
    #unzipfile = zipfile.ZipFile(post);
    #unzipfile.extractall();
    #unzipfile.close();
    ###

    context = {'post': post, 'post_url' : post_url}
    return render(request, 'post_detail.html', context)


