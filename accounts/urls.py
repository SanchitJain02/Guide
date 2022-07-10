from django.urls import path
from .import  views

urlpatterns=[
     #path('',views.index, name='index'),
     path('',views.home, name='home'),
     path('register/',views.register, name='register'),
     path('student_register/',views.student_register.as_view(), name='student_register'),
     path('teacher_register/',views.teacher_register.as_view(), name='teacher_register'),
     path('login/',views.login_request, name='login'),
     path('student_dashboard/',views.student_dashboard, name='student_dashboard'),
     path('teacher_dashboard/',views.teacher_dashboard, name='teacher_dashboard'),
     path('teachers_info/',views.teachers_info, name='teachers_info'),
     path('add_milestones',views.add_milestones, name='add_milestones'),
     path('ask_query',views.ask_query, name='ask_query'),
     path('solve_query',views.solve_query, name='solve_query'),
     path('show_resolved_queries',views.show_resolved_queries, name='show_resolved_queries'),
     path('student_showing_projects',views.student_showing_projects, name='student_showing_projects'),
     path('existing_projects',views.existing_projects, name='existing_projects'),
     path('project_submission',views.project_submission, name='project_submission'),
     path('view_all_projects',views.view_all_projects, name='view_all_projects'),
     path('logout/',views.logout_view, name='logout'),
     path('progress',views.add_progress, name='progress'),
     path('show_progress',views.show_progress, name='show_progress'),
]