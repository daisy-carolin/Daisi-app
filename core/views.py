from django.shortcuts import render
from Student.models import Student
from trainer.models import Trainer
from courses.models import Course
from cal.models import Event


# Create your views here.
def home(request):
    students=Student.objects.count()
    trainers=Trainer.objects.count()
    courses=Course.objects.count()
    events=Event.objects.count()

    data={"students":students,"trainers":trainers,"courses":courses,"events":events}
    return render(request,"home.html",data)

