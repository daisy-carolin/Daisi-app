from django.db import models

# Create your models here.

class Eventscalender(models.Model):

    event_name=models.CharField(max_length=12)

    event_date=models.DateField()

    event_time=models.TimeField()

    event_planner=models.CharField(max_length=25)

    event_participant=models.CharField( max_length=25)

    event_duration=models.TimeField()

    event_approved_by=models.CharField(max_length=25)

    event_id=models.CharField( max_length=25)


        
    