# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.conf.urls import include, url
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Use Case Page (3)
    path('usecase', views.usecase, name='usecase'),

    # Basic Info Page (4)
    path('basic_info', views.basic_info, name='basic_info'),

    # Matches any html file
    url(r'^.*\.*', views.pages, name='pages'),
]
