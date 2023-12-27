from django.shortcuts import render
from django.http import HttpResponse

cities_list = ["Dushanbe", "Khudjand"]

def cities(request):
     return HttpResponse(f"<p>{cities_list[0]}</p><p>{cities_list[1]}</p>")
