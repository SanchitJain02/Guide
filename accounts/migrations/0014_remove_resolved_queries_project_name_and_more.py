# Generated by Django 4.0.3 on 2022-06-11 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_resolved_queries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resolved_queries',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='resolved_queries',
            name='student_name',
        ),
    ]