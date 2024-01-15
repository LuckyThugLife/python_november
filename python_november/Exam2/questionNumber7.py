# Представления  взаимодействуют с моделями и шаблонами.
# Они получают данные из моделей, передают их в шаблоны и возвращают ответ клиенту.

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")


# В Django URL-адреса сопоставляются с представлениями с помощью маршрутизации URL.
# Маршрутизация URL определяет, какие URL-адреса будут обрабатываться какими представлениями.


from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
]


