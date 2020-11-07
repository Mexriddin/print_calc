from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .decorators import unauthenticated_user
from .forms import *


# Create your views here.

@unauthenticated_user
def registerUser(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + username)

            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context=context)

@unauthenticated_user
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    contex = {}
    return render(request, 'accounts/login.html', contex)


def logoutUser(request):
    logout(request)
    return redirect('login')




