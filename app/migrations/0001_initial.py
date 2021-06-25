# Generated by Django 2.2.10 on 2021-06-25 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id_project', models.AutoField(primary_key=True, serialize=False)),
                ('id_user', models.IntegerField(default=0)),
                ('nama_project', models.CharField(max_length=50)),
                ('datecreated', models.DateTimeField()),
                ('dateaccessed', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='step_basic',
            fields=[
                ('id_step_basic', models.AutoField(primary_key=True, serialize=False)),
                ('step_value', models.CharField(max_length=1000)),
                ('step_actor_basic', models.CharField(max_length=20)),
                ('rule', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='usecase',
            fields=[
                ('id_usecase', models.AutoField(primary_key=True, serialize=False)),
                ('nama_usecase', models.CharField(max_length=20)),
                ('brief_description', models.CharField(max_length=300)),
                ('precondition', models.CharField(max_length=100)),
                ('postcondition', models.CharField(max_length=100)),
                ('id_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
            ],
        ),
        migrations.CreateModel(
            name='step_if',
            fields=[
                ('id_step_if', models.AutoField(primary_key=True, serialize=False)),
                ('true_step', models.CharField(max_length=1000)),
                ('false_step', models.CharField(max_length=1000)),
                ('step_actor_true', models.CharField(max_length=20)),
                ('step_actor_false', models.CharField(max_length=20)),
                ('id_step_basic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.step_basic')),
                ('id_usecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usecase')),
            ],
        ),
        migrations.AddField(
            model_name='step_basic',
            name='id_usecase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usecase'),
        ),
        migrations.CreateModel(
            name='step_alternative_flow',
            fields=[
                ('id_step_alternative', models.AutoField(primary_key=True, serialize=False)),
                ('step_alternative', models.CharField(max_length=1000)),
                ('step_actor_alternative', models.CharField(max_length=20)),
                ('condition', models.CharField(max_length=1000)),
                ('id_step_basic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.step_basic')),
                ('id_usecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usecase')),
            ],
        ),
        migrations.CreateModel(
            name='activity_diagram',
            fields=[
                ('id_activity', models.AutoField(primary_key=True, serialize=False)),
                ('nama_activity', models.CharField(max_length=50)),
                ('id_usecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usecase')),
            ],
        ),
    ]
