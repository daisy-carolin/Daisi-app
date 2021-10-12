from django import forms
from django.db.models.base import Model
from django.forms import fields
from django.forms import ModelForm, DateInput
from.models import Event,Event

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
        fields='__all__'

        def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
            self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

