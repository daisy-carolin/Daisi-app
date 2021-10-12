from .models import Course
from django.shortcuts import render
from django.shortcuts import render
from . forms import CoursesRegistrationForm

def register_trainer(request):
    form=CoursesRegistrationForm()
    return render(request,"register_courses.html",{
        "form":form,
        "name":"Daisi Caroline",
    })
def register_courses(request):
    if request.method=="POST":
        form=CoursesRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CoursesRegistrationForm()
    return render(request,"register_courses.html",{"form":form})

def courses_list(request):
    courses=Courses.objects.all()
    return render(request,"courses_list.html",{ "courses":courses})






