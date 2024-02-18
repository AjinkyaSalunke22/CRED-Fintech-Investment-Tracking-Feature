"""
URL configuration for CRED project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from cred_app.views import add_stock, retrive, delete_stock

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_stock/', add_stock, name='add_stock'),
    path('retrive/', retrive, name='retrive'),
    path('delete/<int:id>/', delete_stock, name='delete'),

]
