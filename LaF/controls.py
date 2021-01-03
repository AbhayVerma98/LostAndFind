from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
path('home/', views.home, name='home'),
path('master/', views.master, name='master'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('lost_form/', views.lost_form, name='lost_forms'),
path('lost_people/', views.lost_people, name='lost_people'),
path('search_lost_people/', views.search_lost_people, name='search_lost_people'),
path('find_form/', views.find_form, name='find_forms'),
path('find_people/', views.find_people, name='find_people'),
path('search_find_people/', views.search_find_people, name='search_find_people'),
]
