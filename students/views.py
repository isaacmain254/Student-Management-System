from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Student
from .forms import StudentForm

# Create your views here.
def dashboard(request):
    students = Student.objects.all()
    males = students.filter(gender='male')
    females = students.filter(gender='female')
    in_session = students.filter(status='session')
    # Filter by the year of study
    # queryset = students.order_by('year_of_study')
    # for student in queryset:
    #     data.append(student.year_of_study)
    
    years = students.values('year_of_study').annotate(total_students=Count('id'))
    student_counts = [year['total_students'] for year in years]

    context = {'students': students, 'males': males, 'females': females, 'in_session': in_session, 'student_counts': student_counts }
    return render(request, 'students/dashboard.html', context)

def index(request):
    return render(request, 'students/index.html')

def students_list(request):
    students = Student.objects.all()
    # pagination show # students per page
    paginator = Paginator(students, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'students': students, "page_obj": page_obj}
    return render(request, 'students/students.html', context)

def add_student(request): 
    # Add a new student 
    if request.method != 'POST':
        # no data submitted, create a blank  form 
        form = StudentForm()
    else:
        # Post data submitted ,process data
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:dashboard')
    # Display a blank form or invalid form
    context = {'form' : form}
    return render(request, 'students/add.html', context)