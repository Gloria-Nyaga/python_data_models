from django.db import models

class Course(models.Model):
    course_title = models.CharField(max_length = 20)
    course_category = models.TextField ()
    course_start_date = models.DateField ()
    course_end_date = models.DateField ()
    course_code = models.PositiveSmallIntegerField ()
    teacher_code = models.PositiveSmallIntegerField ()
    student_code = models.PositiveSmallIntegerField ()
    student_number = models.PositiveSmallIntegerField ()
    course_fee = models.PositiveSmallIntegerField ()

# Create your models here.
