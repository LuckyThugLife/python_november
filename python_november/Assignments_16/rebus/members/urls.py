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
    path('cities/', views.cities, name='cities'),
    path('friends/', views.friends, name='friends'),
    path('products/', views.products, name='products'),
    path('cities/details_cities/<int:id>', views.details_cities, name='details_cities'),
    path('friends/details_friends/<int:id>', views.details_friends, name='details_friends'),
    path('products/details_products/<int:id>', views.details_products, name='details_products'),
]
