"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from .views import get_soccer, get_baseball , get_basketball , get_hockey ,get_nfl, BasketballView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/get_nfl', get_nfl),
    url(r'api/get_soccer', get_soccer),
    url(r'api/get_baseball', get_baseball),
    url(r'api/get_basketball', get_basketball),
    url(r'api/get_hockey', get_hockey),
    path('get_baseball', BasketballView.as_view()),
]
