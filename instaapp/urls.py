from re import U
from typing import Pattern
from urllib.parse import urlparse
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import URLPattern, path, include

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
]