# Generated by Django 5.1.2 on 2024-10-25 11:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(related_name='projects_assigned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='UserProject',
        ),
    ]