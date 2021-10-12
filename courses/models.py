from django.db import models

# Create your models here.
class Course(models.Model):

    name=models.CharField(max_length=12)

    course_code=models.CharField(max_length=25)

    syllabus=models.CharField( max_length=15)

    course_trainer=models.CharField( max_length=25)

    course_schedule=models.FileField()

    course_duration=models.CharField(max_length=10)