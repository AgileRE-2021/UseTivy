# Generated by Django 2.2.10 on 2021-06-26 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step_if',
            name='id_usecase',
        ),
    ]
