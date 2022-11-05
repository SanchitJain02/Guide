from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import StudentSignUpForm, TeacherSignUpForm 
from django.contrib.auth.forms import AuthenticationForm
from .models import  Existing_Projects, Milestone, Student, User, New_Project , Teacher, Queries,Resolved_Queries,Progress
from django.contrib.auth import authenticate,login,logout
from twilio.rest import Client
from django.core.mail import send_mail


def home(request):
    return render(request, '../templates/home.html')   


def register(request):
    return render(request, '../templates/register.html')

class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = '../templates/student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class teacher_register(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = '../templates/teacher_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login_request.username = form.cleaned_data.get('username')
            login_request.password = form.cleaned_data.get('password')
            user = authenticate(username=login_request.username, password=login_request.password)
            if user is not None :
                if user.is_student == True:
                    return redirect('student_dashboard')
                else:
                    return redirect('teacher_dashboard')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

def student_dashboard(request):
    students_info = Student.objects.filter(name = login_request.username)
    current_user = {"current_user1":login_request.username}
    context  = {"current_user":current_user,"students_info":students_info}
    return render(request, '../templates/student_dashboard.html',context)
    #return render(request,"customer_dashboard.html")

def teacher_dashboard(request):
    display_project = New_Project.objects.all()
    display_milestones = Milestone.objects.all()
    current_user = {"current_user1":login_request.username}
    context  = {"display_project":display_project,"display_milestones":display_milestones,
    "current_user":current_user}
    return render(request, '../templates/teacher_dashboard.html',context)
    #return render(request,"employee_dashboard.html")       

def project_submission(request):
    students_info_email = Student.objects.get(name = login_request.username)
    students_info = Student.objects.filter(name = login_request.username)
    teachers_name = Teacher.objects.all()
    current_user = {"current_user1":login_request.username}
    context  = {"teachers_name":teachers_name,"current_user":current_user,"students_info":students_info}    
    if request.method == "POST":
        student_name = students_info_email.name
        project_title = request.POST.get("project_title")
        project_desc = request.POST.get("project_desc")
        tech_stack = request.POST.get("tech_stack")
        mentor_name = request.POST.get("mentor_name")
        email_id = students_info_email.email
        new_project = New_Project(student_name = student_name,project_title = project_title,
         project_desc = project_desc,tech_stack = tech_stack,mentor_name = mentor_name,email_id = email_id)
        new_project.save()

        #client = Client("ACf3850645d9ac31dd38c3bbb063f35601","21f4b7dc27febda291d79f39eecbff72")     # ssid,auth token
        #client = Client("AC1cbf3411505257a32ccddb522198e0a5","c50ae7f19b9f34e73c50a11a4e999931")
        #client.messages.create(to=["+91"+phone_no],
                                    #from_ = "+18508015144",
                                    #body = "\n\n Hi "+student_name+" !!! \n\n You have chosen the project -- "+project_title + 
                                    #"\n\n Mentor Name - "+mentor_name + 
                                    #"\n\n Tech stack of the project -"+tech_stack)

        body_student = "\n\n Hii "+student_name+" !!! \n\n You have choosen the project -- "+project_title + "\n\n Mentor Name - "+mentor_name + "\n\n Tech stack of the project - "+tech_stack + "\n\n With Regards \n TEAM GUIDE"
        body_mentor = "\n\n Hii "+mentor_name+" !!! \n\n You have been choosen by : "+student_name+"\n For the project : "+project_title + "\n\n Tech stack of the project - "+tech_stack + "\n\n With Regards \n TEAM GUIDE"
        mentor_info_email = Teacher.objects.get(name = mentor_name)
        email_id_mentor = mentor_info_email.email                          

        send_mail(
            "New Project",
            body_student,
            "jainsanchit625@gmail.com",
            [email_id],
            fail_silently=False
        )

        send_mail(
            "New Project",
            body_mentor,
            "jainsanchit625@gmail.com",
            [email_id_mentor],
            fail_silently=False
        )                            

        messages.success(request,"Project has been submit successfully. A verification message has been sent to your Email id.")
        return redirect("project_submission")    
    return render(request, '../templates/project_submission.html',context)        

   
def add_milestones(request):
    student_projects = New_Project.objects.filter(student_name = login_request.username)
    if request.method == "POST":
        student_name = login_request.username
        project_name = request.POST.get("project_name")
        milestone = request.POST.get("milestone")
        end_date = request.POST.get("end_date")
        new_milestone = Milestone(student_name = student_name,project_name = project_name,
         milestone = milestone,end_date = end_date)
        new_milestone.save()
        messages.success(request,"Milestone has been added successfully")
        return redirect("add_milestones")
    current_user = {"current_user1":login_request.username}   
    context  = {"current_user":current_user,"student_projects":student_projects}    
    return render(request, '../templates/add_milestones.html',context)        

def ask_query(request):
    student_projects = New_Project.objects.filter(student_name = login_request.username)
    if request.method == "POST":
        student_name = login_request.username
        project_name = request.POST.get("project_name")
        query = request.POST.get("query")
        new_query = Queries(student_name = student_name,project_name = project_name,
        query = query)
        new_query.save()
        messages.success(request,"Query has been post successfully")
        return redirect("ask_query")
    current_user = {"current_user1":login_request.username}   
    context  = {"current_user":current_user,"student_projects":student_projects}    
    return render(request, '../templates/ask_query.html',context) 

def solve_query(request):
    if request.method == "POST":
        query = request.POST.get("query")
        query_answer = request.POST.get("query_answer")
        resolved_query = Resolved_Queries(query = query,query_answer =query_answer)
        resolved_query.save()
        messages.success(request,"Query has been resolved successfully")
        return redirect("solve_query")
    query = Queries.objects.all()
    current_user = {"current_user1":login_request.username}   
    context  = {"current_user":current_user,"query":query}
    return render(request, '../templates/solve_query.html',context)     

def show_resolved_queries(request):
    display_resolved_queries = Resolved_Queries.objects.all()
    current_user = {"current_user1":login_request.username}
    context  = {"display_resolved_queries":display_resolved_queries,"current_user":current_user}
    return render(request, '../templates/show_resolved_queries.html',context)

def student_showing_projects(request):
    display_project = New_Project.objects.all()
    display_milestones = Milestone.objects.all()
    students_info = Student.objects.all()
    current_user = {"current_user1":login_request.username}
    context  = {"display_project":display_project,"display_milestones":display_milestones,
    "current_user":current_user,"students_info":students_info}
    return render(request, '../templates/student_showing_projects.html',context)    

def teachers_info(request):
    teachers_details = Teacher.objects.all()
    current_user = {"current_user1":login_request.username}
    context  = {"teachers_details":teachers_details,"current_user":current_user}
    return render(request, '../templates/teachers_info.html',context)  

def view_all_projects(request):
    display_project = New_Project.objects.all()
    context  = {"display_project":display_project}
    return render(request, '../templates/view_all_projects.html',context)  

def existing_projects(request):
    project_details = Existing_Projects.objects.all()
    current_user = {"current_user1":login_request.username}
    context  = {"project_details":project_details,"current_user":current_user}
    return render(request, '../templates/existing_projects.html',context)  

def add_progress(request):
    student_projects = New_Project.objects.filter(student_name = login_request.username)
    current_user = {"current_user1":login_request.username}
    if request.method == "POST":
        student_name = login_request.username
        project_name = request.POST.get("project_name")
        progress = request.POST.get("progress")
        resources = request.POST.get("resources")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        mentor_name_formula = New_Project.objects.get(project_title = project_name)
        mentor_name = mentor_name_formula.mentor_name
        github_username_formula = Student.objects.get(name = student_name)
        github_username = github_username_formula.github_username
        new_progress = Progress(student_name = student_name,project_name = project_name,
         progress = progress,resources = resources,start_date = start_date,
         end_date = end_date,mentor_name = mentor_name,github_username = github_username)
        new_progress.save()
        messages.success(request,"Progress has been submitted successfully")
        return redirect("progress")
    context  = {"student_projects":student_projects,"current_user":current_user}    
    return render(request, '../templates/add_progress.html',context)

def show_progress(request):
    progress_details = Progress.objects.all()
    current_user = {"current_user1":login_request.username}
    context  = {"progress_details":progress_details,"current_user":current_user}
    return render(request, '../templates/show_progress.html',context)


