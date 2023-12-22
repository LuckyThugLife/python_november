from django.shortcuts import render
from django.http import HttpResponse
my_info = {
    "name": "Rustam Sharipov",
    "age": 36,
    "phone": 900555600,
    "@mail": "rustam87.sharipon@gmail.com"
}
def MyProfile(request):
    return HttpResponse(f"<p>{my_info["name"]}</p><p>{my_info["age"]}</p><p>{my_info["phone"]}</p><p>{my_info["@mail"]}</p>")

