# Generated by Django 4.0.3 on 2022-06-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_remove_new_project_phone_no_new_project_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]