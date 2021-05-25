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

    # Use Case Page 
    path('usecase', views.usecase, name='usecase'),

    # Basic Info Page 
    path('basic_info', views.basic_info, name='basic_info'),

    #dashboard
    path('dashboard', views.dashboard, name="dashboard"),

    #create new project
    path('new_project', views.new_project, name="new_project"),

    # Matches any html file
    url(r'^.*\.*', views.pages, name='pages'),
]
