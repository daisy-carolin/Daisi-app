from django import forms
from django.db.models.base import Model
from django.forms import fields

from .models import Eventscalender

class EventscalenderRegistrationForm(forms.ModelForm):
    class Meta:
        model=Eventscalender
        fields="__all__"

