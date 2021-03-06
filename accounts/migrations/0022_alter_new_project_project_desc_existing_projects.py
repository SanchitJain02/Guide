# Generated by Django 4.0.3 on 2022-06-12 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_remove_student_phone_no_new_project_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_project',
            name='project_desc',
            field=models.TextField(max_length=200),
        ),
        migrations.CreateModel(
            name='Existing_Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=150)),
                ('project_desc', models.TextField(max_length=200)),
                ('tech_stack', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=150)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
