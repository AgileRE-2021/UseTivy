# Generated by Django 2.2.10 on 2021-06-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_step_if_id_usecase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step_basic',
            name='rule',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
