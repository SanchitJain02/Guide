# Generated by Django 4.0.6 on 2022-11-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_progress_github_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
