from django.db import models


GENDER_CHOICES = [
    ('male', 'male'), 
    ('female', 'female')
    ]
SESSION_STATUS = [
    ('session', 'In Session'),
      ('holiday', 'On Holiday')
      ]
# Create your models here.
class Student(models.Model):
    registration_no = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    field_of_study = models.CharField(max_length=200)
    year_of_study = models.IntegerField()
    status = models.CharField(max_length=30, choices=SESSION_STATUS)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
