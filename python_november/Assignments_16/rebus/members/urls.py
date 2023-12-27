from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('about_us/', views.about_us, name='about_us'),
    path('news/', views.news, name='news'),
    path('products/', views.products, name='products'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('vacancy/', views.vacancy, name='vacancy'),
]
