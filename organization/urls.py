from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/contacts/', views.contacts, name='contacts'),
    path('about/find-us/', views.find_us, name='find_us'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
]