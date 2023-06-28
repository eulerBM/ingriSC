from django import forms
from register.models import *

class forms_event (forms.ModelForm):
    class Meta:
        model = ticket
        fields = ['user','event_name', 'local', 'day', 'hour']

   