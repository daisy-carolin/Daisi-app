from django.shortcuts import render
from rest_framework import viewsets
from.serializers import StudentSerializer
from Student.models import Student
from.serializers import TrainerSerializer
from trainer.models import Trainer
from.serializers import CourseSerializer
from courses.models import Course
from.serializers import EventSerializer
from.serializers import Event


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class= TrainerSerializer   

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class= CourseSerializer  

class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class= EventSerializer               