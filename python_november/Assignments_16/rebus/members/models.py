from django.db import models

class Cities(models.Model):
    name = models.CharField(max_length=295)
    description = models.TextField(blank=True)
    added_date = models.DateTimeField(auto_now_add=True)



class Products(models.Model):
    name = models.CharField(max_length=295)
    description = models.TextField(blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

class Friends(models.Model):
    name = models.CharField(max_length=295)
    description = models.TextField(blank=True)
    added_date = models.DateTimeField(auto_now_add=True)