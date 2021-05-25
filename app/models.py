# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.
'''
class user(models.Model):
    id_user=models.AutoField(primary_key=True)
    nama_user=models.CharField(max_length=20)
    email_user=models.EmailField()
    password_user=models.CharField(max_length=8)
'''

class project(models.Model):
    id_project=models.AutoField(primary_key=True)
    id_user=models.IntegerField(default=0)
    nama_project=models.CharField(max_length=50)
    datecreated=models.DateTimeField()
    dateaccessed=models.DateTimeField()

class activity_diagram(models.Model):
    id_activity=models.AutoField(primary_key=True)
    id_project=models.ForeignKey(project,on_delete=models.CASCADE)
    nama_activity=models.CharField(max_length=50)
    datecreated=models.DateTimeField()

class basic_flow(models.Model):
    id_basicflow=models.AutoField(primary_key=True)
    id_project=models.ForeignKey(project,on_delete=models.CASCADE)
    steps_basicflow=models.CharField(max_length=1000)
    postcondition_basic=models.CharField(max_length=100)

class usecase(models.Model):
    id_usecase=models.AutoField(primary_key=True)
    id_basicflow=models.ForeignKey(basic_flow,on_delete=models.CASCADE)
    id_project=models.ForeignKey(project,on_delete=models.CASCADE)
    nama_usecase=models.CharField(max_length=20)
    brief_description=models.CharField(max_length=300,default='Add Description Here')
    precondition=models.CharField(max_length=100)
    primary_actor=models.CharField(max_length=20)
    secondary_actor=models.CharField(max_length=20)
    dependency=models.CharField(max_length=30,default='Add Value Here')
    generalization=models.CharField(max_length=30,default='Add Value Here')

class alternative_flow(models.Model):
    id_alternativeflow=models.AutoField(primary_key=True)
    id_usecase=models.ForeignKey(usecase, on_delete=models.CASCADE)
    id_basicflow=models.ForeignKey(basic_flow, on_delete=models.CASCADE)
    type_alternativeflow=models.CharField(max_length=30)
    rfs=models.FloatField(max_length=8)
    steps_alternativeflow=models.CharField(max_length=1000)
    postcondition_alternative=models.CharField(max_length=100)
