# Generated by Django 4.0.3 on 2022-07-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_teacher_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='experience',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
