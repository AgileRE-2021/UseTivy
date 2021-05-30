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

    #form basic flow
    path('basic_flow', views.basic_flow, name="basic_flow"),

    #form specific flow
    path('specific_flow', views.specific_flow, name="specific_flow"),

    #form bounded flow
    path('bounded_flow', views.bounded_flow, name="bounded_flow"),

    #form global flow
    path('global_flow', views.global_flow, name="global_flow"),

    # activity diagram page
    path('activity_diagram', views.activity_diagram, name="activity_diagram"),

    #project view page
    path('project_view', views.project_view, name="project_view"),

    #edit project page
    path('edit_project', views.edit_project, name="edit_project"),

    # Matches any html file
    url(r'^.*\.*', views.pages, name='pages'),
]
