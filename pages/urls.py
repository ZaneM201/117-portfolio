from django.urls import path 
from pages import views

urlpatterns = [
    path('', views.about_view, name='about_me'),
    path('experience/', views.experience_view, name='experience'),
    path('contact/', views.contact_view, name='contact'),
]
