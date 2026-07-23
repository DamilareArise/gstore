"""
URL configuration for gstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from productApp.views import homeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView, name='home'),
    path("products/", include("productApp.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# MVC -> Model, View, Controller, Routers

# MVT - Model, View, Template, urls, forms
# MODEL -> database (ORM) 
# class Users:
#     name
    
# VIEW - CPU of the app in django
# def register():
    # collecting the user input via form operation 
                    # |
    # Store in Users()
    # messages
    # return render(login.html)
    
# URLS 
# route  + function call -> register/  +  register()
