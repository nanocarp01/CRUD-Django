# Generated by Django 3.1.7 on 2021-05-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='descr',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
