from django.urls import path
from . import views

# Defining the namespace for evading a collision betwen app paths
app_name='notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/<int:user_id>', views.about, name='about'),
    path('add/', views.add, name='add')
]