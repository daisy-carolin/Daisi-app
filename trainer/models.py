from django.db import models


# Create your models here.

class Trainer(models.Model):
    first_name=models.CharField(max_length=12)

    last_name=models.CharField(max_length=15)

    course_name=models.CharField(max_length=50)

    GENDER_CHOICES= (
         (U'M' ,U'Male'),
          (U'F' ,U'Female'),
           (U'O' ,U'Others'),
    )  
    gender=models.CharField (max_length=1,choices=GENDER_CHOICES)

    no_of_lessons_taught=models.PositiveBigIntegerField()

    profile=models.ImageField()

    age=models.PositiveIntegerField()
    occupation=models.CharField(max_length=5)

    phone_number=models.CharField(max_length=10)

    bio=models.TextField()
    
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    cv=models.FileField()

    email=models.EmailField(max_length=25)

    contract=models.FileField()

    date_hired=models.DateField(max_length=10)

    LANGUAGE_CHOICES=(
        (u'E', u'English'),
        (u'E', u'Swahili'),
        (u'E', u'Kinyarwanda'),
        (u'E', u'French'),
        (u'E', u'Kiganda'),
   )
    language=models.CharField(max_length=1,choices=LANGUAGE_CHOICES )

