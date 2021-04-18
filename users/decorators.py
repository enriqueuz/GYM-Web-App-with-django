""" Users decorators. """

# Django
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    """ If user is already authenticated redirect him/her to index """
    
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, *kwargs)
    
    return wrapper_func