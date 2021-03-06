# Generated by Django 4.0.3 on 2022-06-08 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_feedback_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='user_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
