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

@login_required(login_url="/login/")
def basic_flow(request):
    
    context = {}
    context['segment'] = 'basic_flow'

    html_template = loader.get_template( 'page/basic_flow.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def specific_flow(request):
    
    context = {}
    context['segment'] = 'specific_flow'

    html_template = loader.get_template( 'page/specific_flow.html' )
    return HttpResponse(html_template.render(context, request)) 

@login_required(login_url="/login/")
def bounded_flow(request):
    
    context = {}
    context['segment'] = 'bounded_flow'

    html_template = loader.get_template( 'page/bounded_flow.html' )
    return HttpResponse(html_template.render(context, request)) 

@login_required(login_url="/login/")
def global_flow(request):
    
    context = {}
    context['segment'] = 'global_flow'

    html_template = loader.get_template( 'page/global_flow.html' )
    return HttpResponse(html_template.render(context, request)) 

@login_required(login_url="/login/")
def activity_diagram(request):
    
    context = {}
    context['segment'] = 'activity_diagram'

    html_template = loader.get_template( 'page/activity_diagram.html' )
    return HttpResponse(html_template.render(context, request)) 