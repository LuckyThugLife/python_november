from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.cities, name='cities'),
]