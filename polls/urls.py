from django.urls import path
#test
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]