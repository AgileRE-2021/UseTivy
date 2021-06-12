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
    actor=models.CharField(max_length=20)
    #secondary_actor=models.CharField(max_length=20)
    #dependency=models.CharField(max_length=30)
    #generalization=models.CharField(max_length=30)

class step_basic(models.Model):
    id_step_basic=models.AutoField(primary_key=True)
    id_usecase=models.ForeignKey(usecase,on_delete=models.CASCADE)
    step_value=models.CharField(max_length=1000)

class alternative_flow(models.Model):
    id_alternativeflow=models.AutoField(primary_key=True)
    id_usecase=models.ForeignKey(usecase, on_delete=models.CASCADE)
    id_step_basic=models.ForeignKey(step_basic,on_delete=models.CASCADE)
    nama_alternative=models.CharField(max_length=200)
    postcondition_alternative=models.CharField(max_length=100)

class step_alternative_flow(models.Model):
    id_step_alternative=models.AutoField(primary_key=True)
    id_alternativeflow=models.ForeignKey(alternative_flow,on_delete=models.CASCADE)
    step_value=models.CharField(max_length=1000)

class activity_diagram(models.Model):
    id_activity=models.AutoField(primary_key=True)
    id_usecase=models.ForeignKey(usecase,on_delete=models.CASCADE)
    nama_activity=models.CharField(max_length=50)
