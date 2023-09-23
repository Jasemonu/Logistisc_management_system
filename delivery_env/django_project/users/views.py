from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegisterUserForm
from .models import User


def register_sender(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.sender = True
            var.save()
            messages.success(request, 'Account. Please login to continue')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect('login')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'users/register_sender.html', context)



def register_rider(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.rider = True
            var.save()
            messages.success(request, 'Account. Please login to continue')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect('register_rider')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'users/register_rider.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'You are logged as {user.username}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'something went wrong. Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Session ended. Please log in to continue')
    return redirect('login')



