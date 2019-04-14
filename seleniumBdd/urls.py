from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('materials/', views.base, name='base'),
    path('create/', views.create_material, name='create'),
]