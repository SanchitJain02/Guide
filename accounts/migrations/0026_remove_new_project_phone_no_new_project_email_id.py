# Generated by Django 4.0.3 on 2022-06-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_rename_experiance_teacher_experience_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_project',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='new_project',
            name='email_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
