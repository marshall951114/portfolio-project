# Generated by Django 2.0.2 on 2020-06-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200606_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.TextField(),
        ),
    ]
