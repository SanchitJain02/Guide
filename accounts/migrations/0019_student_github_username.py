# Generated by Django 4.0.3 on 2022-06-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_rename_highest_degree_student_phone_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='github_username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
