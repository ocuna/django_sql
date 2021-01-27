"""mysql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# need to get the ability to import sub-application urls
from django.conf.urls import include

urlpatterns = [
    path('nvaadmin/', admin.site.urls),
    path('',include('mysql_html.urls')),
    path('',include('mysql_quote.urls')),  
    path('',include('mysql_products.urls')),
    path('',include('mysql_hr.urls')),
    path('',include('mysql_course.urls')),
    path('',include('mysql_CVB.urls')),
]

