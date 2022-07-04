from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Student,Teacher,New_Project
from django.forms import ModelForm


class StudentSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    interest = forms.CharField(required=True)
    highest_degree = forms.CharField(required=True)
    github_username = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.email=self.cleaned_data.get('email')
        student.name=self.cleaned_data.get('name')
        student.interest=self.cleaned_data.get('interest')
        student.email=self.cleaned_data.get('email')
        student.github_username=self.cleaned_data.get('github_username')
        student.save()
        return user

class TeacherSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    interest = forms.CharField(required=True)
    experience = forms.CharField(required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.is_staff = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.email=self.cleaned_data.get('email')
        teacher.name=self.cleaned_data.get('name')
        teacher.interest=self.cleaned_data.get('interest')
        teacher.experience=self.cleaned_data.get('experience')
        teacher.save()
        return user
