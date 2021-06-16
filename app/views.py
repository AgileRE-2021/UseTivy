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
from plantuml import PlantUML
import os
from os.path import abspath

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
    id_url = usecase_target.id_usecase
    #get from request
    namaUseCase = request.POST.get('input-usecase-name')
    briefDes = request.POST.get('input-brief-desc')
    preCondition = request.POST.get('input-precondition')
    postCondition = request.POST.get('input-postcondition')
    #apply in usecase
    usecase_target.nama_usecase = namaUseCase
    usecase_target.brief_description = briefDes
    usecase_target.precondition = preCondition
    usecase_target.postcondition =postCondition

    usecase_target.save()
    
    return redirect('usecase_view',id_usecase=id_url)

@login_required(login_url="/login/")
def add_step_basic(request):
    context = {}
    usecase_target = get_object_or_404(usecase, pk=request.POST.get("id_usecase"))
    id_url = usecase_target.id_usecase

    try:
        stepBasic_target = get_object_or_404(step_basic, pk=request.POST.get("id_step_basic"))
        actorBasic = request.POST.get('actor_input')
        stepBasic_target.step_actor_basic=actorBasic
        stepBasic_target.save()
    except:
        actorBasic = request.POST.get('actor_input')
        stepBasic = request.POST.get('step_input')
        newStepBasic = step_basic(
            step_actor_basic=actorBasic,
            step_value=stepBasic,
            id_usecase=usecase_target
        )
        newStepBasic.save()

    return redirect('edit_use_case',id_usecase=id_url)

@login_required(login_url="/login/")
def edit_step_basic(request, id_step_basic):
    
    context = {}
    context['segment'] = 'edit_step_basic'
    context['id_step_basic'] = id_step_basic
    context['step_basic'] = step_basic.objects.filter(pk=id_step_basic).get()

    return render(request, 'page/edit_step_basic.html', {'context': context})  

@login_required(login_url="/login/")
def update_step_basic(request):
    
    context = {}

    #get from request
    stepbasic_target = get_object_or_404(step_basic, pk=request.POST.get("id_step_basic"))
    id_url=request.POST.get("id_usecase")
    stepActor = request.POST.get("actor_input")
    stepValue = request.POST.get("step_input")

    #update value
    stepbasic_target.step_value = stepValue
    stepbasic_target.step_actor_basic = stepActor
    stepbasic_target.save()

    return redirect('edit_use_case',id_url) 
    # return redirect('dashboard')

@login_required(login_url="/login/")
def delete_step_basic(request,id_step_basic):
    
    stepbasic = step_basic.objects.filter(id_step_basic=id_step_basic).get()
    idUsecase = stepbasic.id_usecase.id_usecase
    stepbasic_target = get_object_or_404(step_basic, pk=id_step_basic).delete()

    return redirect('edit_use_case',id_usecase=idUsecase)


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

    #get use case & project id & nama usecase
    use_case = usecase.objects.filter(id_usecase=id_usecase).get()
    projectID = use_case.id_project.id_project
    useCaseID = use_case.id_usecase
    namaUseCase = use_case.nama_usecase

    #get step basic
    target = step_basic.objects.filter(id_usecase=id_usecase)

    #make the empty txt file
    activity_text = open("activity_"+str(projectID)+"_"+str(useCaseID)+".txt","w+")
    #activity_text.write("@startuml \n")
    activity_text.write("title " +str(namaUseCase)+ "\n")
    i = 1

    for step in target.iterator() :
        if i == 1 :
            #get actor
            actor = step.step_actor_basic
            activity_text.write("|" +(str(actor)).upper()+ "|" + "\n")

            activity_text.write("start \n")

            #get step value
            value_basic = step.step_value
            activity_text.write(":"+ str(value_basic)+ ";" + "\n")
            i = i+1
        else :
            #get actor
            actor = step.step_actor_basic
            activity_text.write("|" +(str(actor)).upper()+ "|" + "\n")

            #get step value
            value_basic = step.step_value
            activity_text.write(":"+ str(value_basic)+ ";" + "\n")
            i = i+1

    activity_text.write("end")
    #activity_text.write("@enduml \n")

    activity_text = open("activity_"+str(projectID)+"_"+str(useCaseID)+".txt","r")

    #generate activity diagram
    server = PlantUML(url='http://www.plantuml.com/plantuml/img/',
                        basic_auth={},
                        form_auth={}, http_opts={}, request_opts={})

    server.processes_file(abspath(f"activity_"+str(projectID)+"_"+str(useCaseID)+".txt"))
        
    return redirect('usecase',id_project=projectID)


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

    
    return render(request, 'page/global_flow.html', {'context' : context})

@login_required(login_url="/login/")
def alternative_step(request,id_step_basic):
    
    context = {}
    context['segment'] = 'alternative_step'
    context['step_basic'] = step_basic.objects.filter(id_step_basic=id_step_basic).get()
    context['step_alternative'] = step_alternative_flow.objects.filter(id_step_basic=id_step_basic)

    return render(request, 'page/alternative_step.html', {'context' : context})

@login_required(login_url="/login/")
def alternative_step_create(request):
    
    context = {}
    actorAlternative = request.POST.get("actor_alternative_input")
    id_stepbasic = request.POST.get("id_step_basic")
    id_usecase = request.POST.get("id_usecase")
    stepAlternative = request.POST.get("step_alternative_input")  
    
    newStepAlternative = step_alternative_flow(
            step_actor_alternative=actorAlternative,
            step_alternative=stepAlternative,
            id_step_basic_id=id_stepbasic,
            id_usecase_id=id_usecase
        )
    newStepAlternative.save()

    return redirect('alternative_step',id_stepbasic)

@login_required(login_url="/login/")
def delete_alternative_step(request,id_step_alternative):
    
    stepalternative = step_alternative_flow.objects.filter(id_step_alternative=id_step_alternative).get()
    idStepbasic = stepalternative.id_step_basic.id_step_basic
    stepalternative_target = get_object_or_404(step_alternative_flow, pk=id_step_alternative).delete()

    return redirect('alternative_step',id_step_basic=idStepbasic)

@login_required(login_url="/login/")
def edit_alternative_step(request, id_step_alternative):
    
    context = {}
    context['segment'] = 'edit_alternative_step'
    context['id_step_alternative'] = id_step_alternative
    context['step_alternative'] = step_alternative_flow.objects.filter(pk=id_step_alternative).get()

    return render(request, 'page/edit_alternative_step.html', {'context': context}) 

@login_required(login_url="/login/")
def update_alternative_step(request):
    
    context = {}

    #get from request
    stepalternative_target = get_object_or_404(step_alternative_flow, pk=request.POST.get("id_step_alternative"))
    id_url=request.POST.get("id_step_basic")
    actorAlternative = request.POST.get("actor_input")
    stepAlternative = request.POST.get("step_input")

    #update value
    stepalternative_target.step_alternative = stepAlternative
    stepalternative_target.step_actor_alternative = actorAlternative
    stepalternative_target.save()

    return redirect('alternative_step',id_url) 
    # return redirect('dashboard') 