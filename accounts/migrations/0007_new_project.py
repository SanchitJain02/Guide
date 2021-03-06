# Generated by Django 4.0.3 on 2022-06-08 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_student_teacher_remove_employee_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100, null=True)),
                ('project_title', models.CharField(max_length=150)),
                ('project_desc', models.TextField()),
                ('tech_stack', models.CharField(max_length=150)),
                ('mentor_name', models.CharField(choices=[('Hardeep Singh', 'HARDEEP SINGH'), ('Mandeep Singh', 'MANDEEP SINGH'), ('Sohil Khan', 'SOHIL KHAN'), ('Salman Khan', 'SALMAN KHAN'), ('Arbaz Khan', 'ARBAZ KHAN')], default='Hardeep Singh', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
