from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    age = models.PositiveSmallIntegerField ()
    code = models.PositiveSmallIntegerField ()
    email = models.EmailField()
    phone_number = models.CharField ( max_length = 20)
    country = models.CharField(max_length = 20)
    salary = models.PositiveBigIntegerField ()
    qualifications = models.TextField ()
    hire_date = models.DateField ()
    gender = models.CharField(max_length = 10)
    bio = models.TextField ()
    picture = models.ImageField ()
    course_code = models.PositiveSmallIntegerField ()

# Create your models here.
