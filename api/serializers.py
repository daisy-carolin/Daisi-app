from rest_framework import serializers
from Student.models import Student
from trainer.models import Trainer
from courses.models import Course
from cal.models import Event

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
            model=Student
            fields=("first_name","last_name","age",)

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
            model=Trainer
            fields=("first_name","last_name","age",)  

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
            model=Course
            fields=("name","course_code","course_trainer",)  

class EventSerializer(serializers.ModelSerializer):
    class Meta:
            model=Event
            fields=("title","description","start_time","end_time")                               