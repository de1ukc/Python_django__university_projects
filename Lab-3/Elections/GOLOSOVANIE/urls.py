from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('elections', views.elections, name='elections')
]