# Generated by Django 4.0.3 on 2022-06-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_existing_projects_interest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='existing_projects',
            name='interest',
            field=models.TextField(max_length=100),
        ),
    ]
