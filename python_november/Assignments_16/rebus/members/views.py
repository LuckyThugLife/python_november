from django.http import HttpResponse
from django.template import loader


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
def products(request):
  template = loader.get_template('products.html')
  return HttpResponse(template.render())
def news(request):
  template = loader.get_template('news.html')
  return HttpResponse(template.render())
def vacancy(request):
  template = loader.get_template('vacancy.html')
  return HttpResponse(template.render())
