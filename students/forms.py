from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
        # labels = {
        #     "registration_no" :' Registration No.',
        #     'first_name': 'First Name',
        #     'last_name': 'Last Name',
        #     'email': 'Email',
        #     'gender': 'gender',
        # }