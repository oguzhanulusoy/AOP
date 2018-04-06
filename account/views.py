from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as login_auth, logout
from .forms import LoginForm, SignUpForm, userEdit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



def deleteMember(request):
    return render(request, 'deleteMember.html', {})

def displayAllMembers(request):
    return render(request, 'displayAllMembers.html', {})


def login(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def home(request):
    return render(request, 'index.html', {})

def login1(request, user):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def login_request(request):
    if request.user.is_authenticated():
        #return HttpResponseRedirect('/index.html')
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            print('here')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login_auth(request, user)
                return HttpResponseRedirect('/')
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_request(request):
    logout(request)
    return redirect('home')

def logout1(request):
    logout(request)
    return render(request, 'logout.html', {})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login1(request, user)
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def display_profile(request, id):
    prof = User.objects.filter(pk=id)[0]

    return render(request, 'profile.html', {'profile':prof})

def userEdit(request, id):
    user = get_object_or_404(User, pk=id) #netten importa bak
    print(user)
    if request.method == 'POST':
        form = userEdit(request.POST, instance = user)
        if form.is_valid():
            user = form.save(commint=False)
            user.email = form.cleaned_data.get('email')

            user.save()
            return redirect('profile.html', id=user.pk)
        #else:
            #return redirect('404.html')
    return redirect('/home')


