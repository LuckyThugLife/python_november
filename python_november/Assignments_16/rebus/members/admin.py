from django.contrib import admin
from .models import Cities, Products, Friends

# Register your models here.
admin.site.register(Cities)
admin.site.register(Products)
admin.site.register(Friends)