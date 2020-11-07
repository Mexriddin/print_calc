from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwars):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwars)

    return wrapper_func