from cgi import print_exception
from sre_constants import CATEGORY_UNI_DIGIT
from tokenize import Name
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
     return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)    
    price = models.IntegerField()
    brand = models.CharField(max_length=50)
    description =models.TextField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True) 
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
     return self.name

class Media(models.Model):
    image = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.COLLAPSE)

    def __str__(self):
     return self.image