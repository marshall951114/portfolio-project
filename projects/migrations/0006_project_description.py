# Generated by Django 2.0.2 on 2020-06-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_project_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='default'),
        ),
    ]