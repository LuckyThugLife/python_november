from django.http import HttpResponse
from django.template import loader
from .models import Cities, Friends, Products

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())
def about_us(request):
  template = loader.get_template('about_us.html')
  return HttpResponse(template.render())
def services(request):
  template = loader.get_template('services.html')
  return HttpResponse(template.render())
def projects(request):
  template = loader.get_template('projects.html')
  return HttpResponse(template.render())

def news(request):
  template = loader.get_template('news.html')
  return HttpResponse(template.render())
def vacancy(request):
  template = loader.get_template('vacancy.html')
  return HttpResponse(template.render())

def products(request):
    myproducts = Products.objects.all().values()
    template = loader.get_template('products.html')
    context = {
        'myproducts': myproducts
    }
    return HttpResponse(template.render(context, request))

def cities(request):
    mycities = Cities.objects.all().values()
    template = loader.get_template('cities.html')
    context = {
      'mycities': mycities,
    }
    return HttpResponse(template.render(context, request))

def friends(request):
    myfriends = Friends.objects.all().values()
    template = loader.get_template('friends.html')
    context = {
        'myfriends': myfriends
    }
    return HttpResponse(template.render(context, request))

def details_cities(request, id):
  mycities = Cities.objects.get(id=id)
  template = loader.get_template('details_cities.html')
  context = {
    'mycities': mycities,
  }
  return HttpResponse(template.render(context, request))

def details_friends(request, id):
  myfriends = Friends.objects.get(id=id)
  template = loader.get_template('details_friends.html')
  context = {
    'myfriends': myfriends,
  }
  return HttpResponse(template.render(context, request))

def details_products(request, id):
  myproducts = Products.objects.get(id=id)
  template = loader.get_template('details_products.html')
  context = {
    'myproducts': myproducts,
  }
  return HttpResponse(template.render(context, request))