from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Student,Teacher,New_Project
from django.forms import ModelForm


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
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
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.name=self.cleaned_data.get('username')
        student.email=self.cleaned_data.get('email')
        student.interest=self.cleaned_data.get('interest')
        student.email=self.cleaned_data.get('email')
        student.github_username=self.cleaned_data.get('github_username')
        student.save()
        return user

class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
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
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.email=self.cleaned_data.get('email')
        teacher.name=self.cleaned_data.get('username')
        teacher.interest=self.cleaned_data.get('interest')
        teacher.experience=self.cleaned_data.get('experience')
        teacher.save()
        return user
