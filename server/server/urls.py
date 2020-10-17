"""server URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

app_name = 'backend'
urlpatterns = [
    path('api/hello/', views.hello, name='hello'),
]

urlpatterns += [
    path('0/1', views.lighton, name='lighton'),
    path('0/0', views.lightoff, name='lightoff'),
    path('0/red', views.red, name='red'),
    path('0/green', views.green, name='green'),
    path('0/blue', views.blue, name='blue'),
    path('0/yellow', views.yellow, name='yellow'),
    path('0/janne', views.janne, name='janne'),
    path('0/disco', views.disco, name='disco'),
    url(r'0/lights/(\w{6})/(\d+)', views.lights, name='lights'),
]