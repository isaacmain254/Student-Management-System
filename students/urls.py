from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.students_list, name='students_list'),
    path('students/<int:id>/', views.student_details, name='student-details'),
    path('add_student/', views.add_student, name='add'),
    path('edit/<int:student_id>/', views.edit_details, name='edit_details'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('search/', views.search_student, name='search' ),
]