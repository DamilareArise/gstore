from django.contrib import admin
from .models import Category, Brand, Product, ProductImages, ProductSpecification 

# Register your models here.

admin.site.register([Category, Brand, Product, ProductImages, ProductSpecification])
