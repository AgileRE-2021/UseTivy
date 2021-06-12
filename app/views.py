# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, request
from django import template
from app.models import project, usecase, step_basic, alternative_flow, step_alternative_flow, activity_diagram
from django.utils import timezone

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

'''
----------DASHBOARD & PROJECT----------
'''

@login_required(login_url="/login/")
def dashboard(request):
    
    context = {}
    context['segment'] = 'dashboard'
    context['project'] = project.objects.filter(id_user=request.user.id)

    return render(request, 'page/dashboard.html', {'context': context})   

@login_required(login_url="/login/")
def new_project(request):
    
    context = {}
    context['segment'] = 'new_project'

    return render(request,'page/new_project.html') 

@login_required(login_url="/login/")
def create_project(request):
    
    namaProject = request.POST.get("nama_project")
    dateCreated=timezone.now()
    dateAccessed=timezone.now()

    newProject = project(
        id_user=request.user.id,
        nama_project=namaProject,
        datecreated=dateCreated,
        dateaccessed=dateAccessed
    )

    newProject.save()

    return redirect('dashboard')  

@login_required(login_url="/login/")
def edit_project(request, id_project):
    
    context = {}
    context['segment'] = 'edit_project'
    context['id_project'] = id_project
    context['project'] = project.objects.filter(pk=id_project).get()

    return render(request, 'page/edit_project.html', {'context': context})  

@login_required(login_url="/login/")
def update_project(request):
    
    context = {}
    project_target = get_object_or_404(project, pk=request.POST.get("id_project"))
    projectName = request.POST.get("nama_project")

    #update value
    project_target.nama_project = projectName
    project_target.dateaccessed = timezone.now()
    project_target.save()

    return redirect('dashboard') 

@login_required(login_url="/login/")
def delete_project(request, id_project):
    
    project_target = get_object_or_404(project, pk=id_project).delete()
    return redirect('dashboard')  


'''
----------USE CASE----------
'''


@login_required(login_url="/login/")
def use_case(request,id_project):
    
    context = {}
    context['segment'] = 'usecase'
    context['project'] = id_project
    context['name'] = project.objects.filter(id_project=id_project).get()
    context['use_case'] = usecase.objects.filter(id_project=context['project'])

    return render(request, 'page/use_case.html', {'context': context})
    
@login_required(login_url="/login/")
def usecase_view(request,id_usecase):
    
    context = {}
    context['segment'] = 'usecase_view'
    context['use_case'] = usecase.objects.filter(id_usecase=id_usecase).get()
    context['step_basic'] = step_basic.objects.filter(id_usecase=id_usecase)

    return render(request, 'page/usecase_view.html', {'context': context})

@login_required(login_url="login/")
def new_usecase(request,id_project):
    
    context = {}
    context['segment'] = 'new_usecase'
    context['id_project'] = id_project
    context['project'] = project.objects.filter(id_project=id_project).get()

    return render(request,'page/new_use_case.html', {'context': context})

@login_required(login_url="login/")
def usecase_create(request):
    
    namaUseCase = request.POST.get("nama_usecase")
    idProject = request.POST.get("id_project")
    project_target = project.objects.filter(id_project=idProject).get()

    newUseCase = usecase(
        nama_usecase=namaUseCase,
        id_project=project_target
    )

    newUseCase.save()

    return redirect('usecase',id_project=idProject )

@login_required(login_url="/login/")
def edit_use_case(request,id_usecase):
    
    context = {}
    context['segment'] = 'edit_project'
    context['use_case'] = usecase.objects.filter(id_usecase=id_usecase).get()
    context['step_basic'] = step_basic.objects.filter(id_usecase=id_usecase)

    return render(request, 'page/edit_use_case.html', {'context' : context})

@login_required(login_url="/login/")
def update_use_case(request):

    context = {}
    usecase_target = get_object_or_404(usecase, pk=request.POST.get("id_usecase"))
    id_url = usecase_target.id_project.id_project

    #get from request
    namaUseCase = request.POST.get('input-usecase-name')
    briefDes = request.POST.get('input-brief-desc')
    preCondition = request.POST.get('input-precondition')
    postCondition = request.POST.get('input-postcondition')
    #primaryActor = request.POST.get('input-prim-actor')
    #secondaryActor = request.POST.get('input-sec-actor')
    #dependency_input = request.POST.get('input-depedency')
    #generalization_input = request.POST.get('input-generalization')

    #apply in usecase
    usecase_target.nama_usecase = namaUseCase
    usecase_target.brief_description = briefDes
    usecase_target.precondition = preCondition
    usecase_target.postcondition =postCondition
    #usecase_target.primary_actor = primaryActor
    #usecase_target.secondary_actor = secondaryActor
    #usecase_target.dependency =  dependency_input
    #usecase_target.generalization = generalization_input

    usecase_target.save()
    
    return redirect('usecase',id_project=id_url)

@login_required(login_url="/login/")
def delete_use_case(request,id_usecase):
    
    use_case = usecase.objects.filter(id_usecase=id_usecase).get()
    idProject = use_case.id_project.id_project
    usecase_target = get_object_or_404(usecase, pk=id_usecase).delete()

    return redirect('usecase',id_project=idProject)


'''
----------  ACTIVITY DIAGRAM  ----------
'''


@login_required(login_url="/login/")
def activity_diagram(request,id_usecase):

    context = {}
    context['segment'] = 'activity_diagram'
    #get use case
    use_case = usecase.objects.filter(id_usecase=id_usecase).get()
    #get step basic
    step_basic_target = step_basic.objects.filter(id_usecase=id_usecase)

    for (step, i) in  step_basic_target :
        #get actor
        actor_basic = step.step_actor_basic
        #get step value
        value_basic = step.step_value
        


    
    return render(request, 'page/activity_diagram.html', {'context': context}) 


'''
----------  FLOW  ----------
'''


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

