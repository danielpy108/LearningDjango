from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, NoteSerializer
from notes.models import User, Note
from django.shortcuts import Http404

@api_view(['GET'])
def overview(request):
    api_urls = {
        'List': [ '/user-list/', 
                  '/notes-list/'],
        'Detail View': [ '/user/<str:user_name>',
                         '/note/<int:pk>'],
        'Create': [ '/user-create/', 
                   '/notes-create/'],
        'Update': [ '/user-update/<int:pk>',
                    '/notes-update/<int:pk>/'],
        'Delete': [ 
                    '/user-delete/<str:user_name>'
                    '/notes-delete/<int:pk>/']
    }
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)    # manay is True if we pass a list of objects, else False for a single object
    return Response(serializer.data)

@api_view(['GET'])
def noteList(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailViewUser(request, user_name):
    try:
        user = User.objects.get(user_name=user_name)
    except(User.DoesNotExist):
        return Http404("Fuck u, it doesn't exist")
    else:
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)