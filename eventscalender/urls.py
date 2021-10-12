
from django.urls import path
from.views import register_eventscalender
from.views import  eventscalender_list


urlpatterns = [
    path("register",register_eventscalender,name="register_Eventscalender"),
    path("list/",eventscalender_list,name="eventscalender_list"),
]
