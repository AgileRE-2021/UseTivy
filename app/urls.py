# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.conf.urls import include, url
from app import views

urlpatterns = [

    # The home page
    path('', views.dashboard, name='home'),

    # Basic Info Page 
    path('basic_info', views.basic_info, name='basic_info'),

    #dashboard
    path('dashboard', views.dashboard, name="dashboard"),

    #-------------PROJECT-------------
    #create new project
    path('new_project', views.new_project, name="new_project"),
    path('new_project/create', views.create_project, name="create_project"),

    #edit project page
    path('edit_project/<int:id_project>', views.edit_project, name="edit_project"),
    path('edit_project/update', views.update_project, name="update_project"),

    #delete project
    path('delete_project/<int:id_project>', views.delete_project, name="delete_project"),



    #-------------USE CASE-------------
    # Use Case Page 
    path('use_case/<int:id_project>', views.use_case, name='usecase'),

    #view use case page
    path('usecase_view/<int:id_usecase>', views.usecase_view, name="usecase_view"),

    #create use case
    path('new_usecase/<int:id_project>', views.new_usecase, name="new_usecase"),
    path('usecase_create',views.usecase_create, name="usecase_create"),

    #edit use caase
    path('edit_use_case/<int:id_usecase>', views.edit_use_case, name="edit_use_case"),
    path('edit_use_case/update', views.update_use_case, name="update_use_case"),

    #delete use case
    path('delete_use_case/<int:id_usecase>', views.delete_use_case, name="delete_use_case"),

    #delete step basic
    path('delete_step_basic/<int:id_step_basic>', views.delete_step_basic, name="delete_step_basic"),

     #------------- FLOW -------------
    #form basic flow
    path('basic_flow', views.basic_flow, name="basic_flow"),

    #form specific flow
    path('specific_flow', views.specific_flow, name="specific_flow"),

    #form bounded flow
    path('bounded_flow', views.bounded_flow, name="bounded_flow"),

    #form global flow
    path('global_flow', views.global_flow, name="global_flow"),

    #create alternative step
    path('alternative_step/<int:id_step_basic>', views.alternative_step, name="alternative_step"),
    path('alternative_step_create',views.alternative_step_create, name="alternative_step_create"),

    #delete step basic
    path('delete_alternative_step/<int:id_step_basic>', views.delete_alternative_step, name="delete_step_basic"),

     #-------------ACTIVITY DIAGRAM------------
    # activity diagram page
    path('activity_diagram/<int:id_usecase>', views.activity_diagram, name="activity_diagram"),


    # Matches any html file
    url(r'^.*\.*', views.pages, name='pages'),
]
