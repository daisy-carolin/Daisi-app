from .models import Eventscalender
from django.shortcuts import render


# Create your views here.
from os import name
from django.forms.forms import Form
from django.shortcuts import render
from .forms import EventscalenderRegistrationForm


def register_eventscalender(request):
    form=EventscalenderRegistrationForm()
    return render(request,"register_eventscalender.html",{
        "form":form,
        "name":"Daisi Caroline",
    })
def register_eventscalender(request):
    if request.method=="POST":
        form=EventscalenderRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=EventscalenderRegistrationForm()
    return render(request,"register_eventscalender.html",{"form":form})

def eventscalender_list(request):
    eventscalenders=Eventscalender.objects.all()
    return render(request,"eventscalender_list.html",{ "eventscalenders":eventscalenders})

