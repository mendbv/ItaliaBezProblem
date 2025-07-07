from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('mission-vision/', views.mission_vision, name='mission_vision'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('contact-popup/', views.contact_popup, name='contact_popup'),
]
