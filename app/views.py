# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, request
from django import template

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))   

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def dashboard(request):
    
    context = {}
    context['segment'] = 'dashboard'

    html_template = loader.get_template( 'page/dashboard.html' )
    return HttpResponse(html_template.render(context, request))   

@login_required(login_url="/login/")
def new_project(request):
    
    context = {}
    context['segment'] = 'new_project'

    html_template = loader.get_template( 'page/new_project.html' )
    return HttpResponse(html_template.render(context, request)) 

@login_required(login_url="/login/")
def usecase(request):
    
    context = {}
    context['segment'] = 'usecase'

    html_template = loader.get_template( 'page/usecase.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def basic_info(request):
    
    context = {}
    context['segment'] = 'basic_info'

    html_template = loader.get_template( 'page/basic_info.html' )
    return HttpResponse(html_template.render(context, request)) 