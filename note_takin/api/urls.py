from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('user-list/', views.userList, name='user-list'),
    path('note-list/', views.noteList, name='note-list'),
    path('user/<str:user_name>', views.detailViewUser, name='detail-view-user')
]