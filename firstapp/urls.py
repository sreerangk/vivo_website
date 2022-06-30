from django.urls import path
from .import views

urlpatterns = [
    path('GHJK', views.index, name='index'),
    path('', views.base, name='base'),
]