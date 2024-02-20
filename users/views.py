from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages




def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Invalid Username or Password')
            return redirect('login_user')
    return render(request, 'users/login_user.html') 


def logout_user(request):
    logout(request)
    messages.success(request, 'You were logged out')
    return redirect('/')


def register_user(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registraton successsful')
            return redirect('/') 
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'users/register_user.html', {'form':form})
