from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
# from django.db.models import Q
from .models import Student
from .forms import StudentForm

# Create your views here.
@login_required
def dashboard(request):
    students = Student.objects.all()
    males = students.filter(gender='male')
    females = students.filter(gender='female')
    in_session = students.filter(status='session')
  
    years = students.values('year_of_study').annotate(total_students=Count('id'))
    student_counts = [year['total_students'] for year in years]

    context = {'students': students, 'males': males, 'females': females, 'in_session': in_session, 'student_counts': student_counts }
    return render(request, 'students/dashboard.html', context)

def index(request):
    return render(request, 'students/index.html')

@login_required
def students_list(request):
    search_query = request.GET.get('q')
    # search for student 
    if search_query:
        students = Student.objects.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(registration_no__icontains=search_query) | Q( year_of_study__icontains=search_query))

    else: 
        students = Student.objects.all()
    # pagination show # students per page
    paginator = Paginator(students, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'students': students, "page_obj": page_obj }
    return render(request, 'students/students.html', context)

# view student deyails 
def student_details(request, id):
    student = Student.objects.get(pk=id)
    return redirect('students:students_list')

# search for a student 
def search_student(request):
    query = request.GET.get('q')
    if query: 
     # search queryset
        search_query = Student.objects.filter(first_name__icontains=query)
    else: 
        search_query
    # pagination
    paginator = Paginator(search_query,8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'search_query': search_query, 'page_obj': page_obj}
    return render(request, 'students/search.html', context)


@login_required
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

def edit_details(request, student_id):
    # edit an existing student details
    student = Student.objects.get(id=student_id)

    if request.method != 'POST':
        # INITIAL REQUSET PREFILL FORM WITH EXISTING DETAILS
        form = StudentForm(instance=student)
    
    else:
        # process and submit data
        form = StudentForm(instance=student, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:students_list')

    context = {'student': student, 'form': form}
    return render(request, 'students/edit_details.html', context)


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('students:students_list')