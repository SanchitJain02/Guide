from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import datetime

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length=50,null = True)
    email = models.CharField(max_length=50)
    interest = models.CharField(max_length=50)
    github_username = models.CharField(max_length=100,null = True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length=50,null = True)
    email = models.CharField(max_length=50)
    interest = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class New_Project(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    student_name = models.CharField(max_length=100,null = True)
    project_title = models.CharField(max_length=150)
    project_desc = models.TextField(max_length=200)
    tech_stack = models.CharField(max_length=150)
    mentor_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length = 100,null = True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.project_title

class Milestone(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    student_name = models.CharField(max_length=100,null = True)
    project_name = models.CharField(max_length=150)
    milestone = models.CharField(max_length=150)
    end_date = models.CharField(max_length=150)

    def __str__(self):
        return self.project_name
       
class Queries(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    student_name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=150)
    query = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name   

class Resolved_Queries(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    student_name = models.CharField(max_length=100,null = True)
    project_name = models.CharField(max_length=150,null = True)
    query = models.CharField(max_length=200)
    query_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.query              

class Existing_Projects(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    project_name = models.CharField(max_length=150)
    project_desc = models.TextField(max_length=400)
    interest = models.TextField(max_length=100)
    tech_stack = models.CharField(max_length=150)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.project_name                 

class Progress(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    student_name = models.CharField(max_length=100,null = True)
    project_name = models.CharField(max_length=150)
    start_date = models.CharField(max_length=150)
    end_date = models.CharField(max_length=150)
    progress = models.CharField(max_length=300)
    resources = models.CharField(max_length=300)
    mentor_name = models.CharField(max_length=100,null = True)
    github_username = models.CharField(max_length=100,null = True)

    def __str__(self):
        return self.project_name