from django.urls import path
from . import views

urlpatterns = [
    path('MyProfile/', views.MyProfile, name='MyProfile'),
]