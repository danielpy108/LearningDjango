from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User, Note

def index(request):
    users = User.objects.all()                                       # Get all fuckin users
    return render(request, 'notes/index.html', {'users': users})     # Render them

def about(request, user_id):
    try:
        user = get_object_or_404(User, pk=user_id)                       # Get the fucking pk of the user
    except (KeyError, User.DoesNotExist):
        return render(request, 'notes/about.html', {'user': user, 
                                                    'error_msg': 'The user_id doesn\'t exist'})
    else:
        return render(request, 'notes/about.html', {'user': user})       # Render it 4 displaying its data

def add(request):
    users = User.objects.all()
    return render(request, 'notes/add.html', {'users': users})