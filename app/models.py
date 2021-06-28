# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.

class project(models.Model):
    id_project=models.AutoField(primary_key=True)
    id_user=models.IntegerField(default=0)
    nama_project=models.CharField(max_length=50)
    datecreated=models.DateTimeField()
    dateaccessed=models.DateTimeField()

class usecase(models.Model):
    id_usecase=models.AutoField(primary_key=True)
    id_project=models.ForeignKey(project,on_delete=models.CASCADE)
    nama_usecase=models.CharField(max_length=20)
    brief_description=models.CharField(max_length=300)
    precondition=models.CharField(max_length=100)
    postcondition=models.CharField(max_length=100)

class step_basic(models.Model):
    id_step_basic=models.AutoField(primary_key=True)
    id_usecase=models.ForeignKey(usecase,on_delete=models.CASCADE)
    step_value=models.CharField(max_length=1000)
    step_actor_basic=models.CharField(max_length=20)
    rule=models.CharField(max_length=5, default='0')

class step_if(models.Model):
    id_step_if =models.AutoField(primary_key=True)
    id_step_basic=models.ForeignKey(step_basic,on_delete=models.CASCADE)
    id_usecase=models.ForeignKey(usecase,on_delete=models.CASCADE)
    true_step=models.CharField(max_length=1000)
    false_step=models.CharField(max_length=1000)    
    step_actor_true=models.CharField(max_length=20)
    step_actor_false=models.CharField(max_length=20)

class step_alternative_flow(models.Model):
    id_step_alternative=models.AutoField(primary_key=True)
    id_step_basic=models.ForeignKey(step_basic,on_delete=models.CASCADE)
    id_usecase=models.ForeignKey(usecase, on_delete=models.CASCADE)
    step_alternative=models.CharField(max_length=1000)
    step_actor_alternative=models.CharField(max_length=20)
    condition=models.CharField(max_length=1000)   

class activity_diagram(models.Model):
    id_activity=models.AutoField(primary_key=True)
    id_usecase=models.ForeignKey(usecase,on_delete=models.CASCADE)
    nama_activity=models.CharField(max_length=50)
